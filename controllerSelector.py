import maya.cmds as cmds
import sys
import maya.OpenMaya as OpenMaya
from functools import partial
import configLoader
reload(configLoader)
import controllerManager
reload(controllerManager)

WINDOW_ID = "ctrlSelector"
WINDOW_TITLE = "Animation Picker 1.0"

root_path = ""
conf = None # ConfigLoader object
ctrlManager = None
ctrlSelectorWindow = None # Window object for the controller selector
rig_background_img = None # RIG image, displayed in background
selectionEventListener = None

def create_window(conf, window, tabs, width, height):
    print "Creating window "+WINDOW_ID
    window = cmds.window(WINDOW_ID,t=WINDOW_TITLE, sizeable=True, resizeToFitChildren=True)
    cmds.rowLayout( numberOfColumns=2, columnWidth=(1, 150), columnAttach=[(1, 'both', 0), (2, 'both', 0)], rowAttach=[(1, "top", 10), (2, "top", 0)] )
    cmds.columnLayout( columnAttach=('both', 5), rowSpacing=10, adj=True )
    
    cmds.iconTextButton(style="iconOnly", image=root_path+"logo.png", highlightImage=root_path+"logo.png", height=165, width=140, command=clear_selection)

    for tab_button in ctrlManager.tab_buttons: 
        b = cmds.button("tab_"+tab_button.name, label="Select "+tab_button.name, backgroundColor=tab_button.color)
        tab_button.set_ui("tab_"+tab_button.name)
        cmds.button(b, edit=True, command=partial(tab_button_callback, tab_button))

    cmds.setParent("..")
    
    tabLayout = cmds.tabLayout(height=height+20, width=width)
    
    for name, background in tabs.iteritems():
        # Configure tab in formLayout
        form = cmds.formLayout()
        cmds.tabLayout(tabLayout, edit=True, tabLabel=[form, name])
        cmds.image(image=root_path+background)
        add_buttons(conf.buttons, form, name)
        add_group_buttons(conf.group_buttons, form, name)
        cmds.setParent("..")

def add_buttons(buttons, layout, tab):
    for button in buttons:
        if button.tab == tab:
            b = cmds.iconTextButton(button.controller, style="iconOnly", image=root_path+button.color, height=button.height, width=button.width)
            button.set_ui(button.controller)
            cmds.iconTextButton(b, edit=True, command=partial(button_callback, button))
            cmds.formLayout( layout, edit=True, attachForm=[(b, 'top', button.top_offset), (b, 'left', button.left_offset)])

def add_group_buttons(buttons, layout, tab):
    for button in buttons:
        if button.tab == tab:
            b = cmds.iconTextButton(button.group, style="iconOnly", width=20, height=20, image=root_path+button.path)
            button.set_ui(button.group)
            cmds.iconTextButton(b, edit=True, command=partial(group_button_callback, button))
            cmds.formLayout( layout, edit=True, attachForm=[(b, 'top', button.top_offset), (b, 'left', button.left_offset)])

def button_callback(button, *args):
    if not button.is_selected(): # If the button is currently not selected, but it must be :
        ctrlManager.add_controller_to_selection(button.controller)
    else: # If the buttonn is currently selected, but is must not be :
        ctrlManager.remove_controller_from_selection(button.controller)
    cmds.select( ctrlManager.get_selection_list() )

def group_button_callback(group_button, *args):
    if not group_button.is_selected(): # If the button is currently not selected, but it must be :
        for button in group_button.get_associated_buttons():
            ctrlManager.add_controller_to_selection(button.controller)
    else: # If the buttonn is currently selected, but is must not be :
        for button in group_button.get_associated_buttons():
            ctrlManager.remove_controller_from_selection(button.controller)
    cmds.select( ctrlManager.get_selection_list() )

def selection_event_callback(*args, **kwargs):
    really_selected_controllers = cmds.ls( selection=True )
    # Remove controllers which have been unselected 
    for controller in ctrlManager.get_selection_list():
        if controller not in really_selected_controllers:
            ctrlManager.remove_controller_from_selection(controller)
    # Add controllers which have been manually selected in maya
    for controller in really_selected_controllers:
        if controller not in ctrlManager.get_selection_list():
            ctrlManager.add_controller_to_selection(controller)
    # Toggle selected buttons and check UI
    selection_list = ctrlManager.get_selection_list()
    for button in ctrlManager.buttons:
        if button.controller in selection_list:
            button.select()
        else:
            button.unselect()
        cmds.iconTextButton(button.get_ui(), edit=True, image=root_path+button.color) 
    # Update group buttons
    for group_button in ctrlManager.group_buttons:
        if group_button.must_be_selected():
            group_button.select()
        else:
            group_button.unselect()
        cmds.iconTextButton(group_button.get_ui(), edit=True, image=root_path+group_button.path)
    # Update tab buttons
    for tab_button in ctrlManager.tab_buttons:
        if tab_button.must_be_selected():
            tab_button.select()
        else:
            tab_button.unselect()
        cmds.button(tab_button.get_ui(), edit=True, backgroundColor=tab_button.color)


def tab_button_callback(tab_button, *args):
    if not tab_button.is_selected(): # If the button is currently not selected, but it must be :
        for button in tab_button.get_associated_buttons():
            ctrlManager.add_controller_to_selection(button.controller)
    else: # If the buttonn is currently selected, but is must not be :
        for button in tab_button.get_associated_buttons():
            ctrlManager.remove_controller_from_selection(button.controller)
    cmds.select( ctrlManager.get_selection_list() )
    
def clear_selection(*args):
    ctrlManager.clear_selection()
    cmds.select( ctrlManager.get_selection_list() )
    
def main(path):
    global ctrlManager, selectionEventListener, root_path
    
    # Setting root path
    root_path = path
    
    # If the window is currently open, let's close it
    if cmds.window(WINDOW_ID, exists = True):
        print "Window "+WINDOW_ID+" already exists. Closing the existing window."
        cmds.deleteUI(WINDOW_ID)
        
    # Load configuration file
    conf = configLoader.ConfigLoader(root_path+"config.json")
    conf.parse()
      
    # Creating controller manager 
    ctrlManager = controllerManager.ControllerManager(conf.buttons, conf.group_buttons, conf.tab_buttons)
    
    # Create the window container
    create_window(conf, ctrlSelectorWindow, conf.tabs, conf.width, conf.height)
    cmds.showWindow(WINDOW_ID)
    
    # Adding selection event listener
    selectionEventListener = OpenMaya.MEventMessage.addEventCallback("SelectionChanged", selection_event_callback)
    
    # Forcing initial selection sync
    selection_event_callback()
    

if __name__ == "__main__":
    path = r"C:\Users\sylva\Documents\maya\2019\scripts\controllerSelector\\"
    if len(sys.argv) >= 2:
        path = sys.argv[1]
    main(path)
    

    