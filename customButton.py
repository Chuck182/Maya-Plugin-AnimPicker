class Button():
    def __init__(self, controller, width, height, top_offset, left_offset, s_color, u_color, tab, groups):
        self._controller = controller
        self._width = width
        self._height = height
        self._top_offset = top_offset
        self._left_offset = left_offset
        self._unselected_color = u_color
        self._selected_color = s_color
        self._is_selected = False
        self._groups = groups
        self._ui = None
        self._tab = tab
        
    @property
    def controller(self):
        return self._controller
    
    @property
    def width(self):
        return self._width
        
    @property
    def height(self):
        return self._height
        
    @property
    def top_offset(self):
        return self._top_offset
        
    @property
    def left_offset(self):
        return self._left_offset
        
    @property
    def groups(self):
        return self._groups
        
    @property
    def color(self):
        path = self._unselected_color
        if self._is_selected:
            path = self._selected_color
        return path
        
    @property
    def tab(self):
        return self._tab
        
    def toggle(self):
        if self._is_selected:
            self._is_selected = False
        else:
            self._is_selected = True
            
    def is_selected(self):
        return self._is_selected
        
    def select(self):
        self._is_selected = True
    
    def unselect(self):
        self._is_selected = False
    
    def set_ui(self, ui):
        self._ui = ui
        
    def get_ui(self):
        return self._ui
        
class GroupButton():
    def __init__(self, group, top_offset, left_offset, s_path, u_path, tab):
        self._group = group
        self._top_offset = top_offset
        self._left_offset = left_offset
        self._s_path = s_path
        self._u_path = u_path
        self._is_selected = False
        self._ui = None
        self._buttons = []
        self._tab = tab

    @property
    def group(self):
        return self._group
        
    @property
    def tab(self):
        return self._tab
        
    @property
    def top_offset(self):
        return self._top_offset
        
    @property
    def left_offset(self):
        return self._left_offset
    
    @property
    def path(self):
        path = self._u_path
        if self._is_selected:
            path = self._s_path
        return path
    
    def toggle(self):
        if self._is_selected:
            self._is_selected = False
        else:
            self._is_selected = True
            
    def is_selected(self):
        return self._is_selected
        
    def select(self):
        self._is_selected = True
    
    def unselect(self):
        self._is_selected = False

    def set_ui(self, ui):
        self._ui = ui
        
    def get_ui(self):
        return self._ui
        
    def add_button(self, button):
        self._buttons.append(button)
        
    def get_associated_buttons(self):
        return self._buttons

        
    def must_be_selected(self):
        mustbe = True
        for button in self._buttons:
            if not button.is_selected():
                mustbe =False
                break
        return mustbe
        
class TabButton():
    def __init__(self, name):
        self._name = name
        self._selected_color = (0.86,0.55,0.38)
        self._unselected_color = (0.4,0.4,0.4)
        self._is_selected = False
        self._ui = None
        self._buttons = []
        self._group_buttons = []

    @property
    def name(self):
        return self._name
            
    @property
    def color(self):
        color = self._unselected_color
        if self._is_selected:
            color = self._selected_color
        return color
    
    def toggle(self):
        if self._is_selected:
            self._is_selected = False
        else:
            self._is_selected = True
            
    def is_selected(self):
        return self._is_selected
        
    def select(self):
        self._is_selected = True
    
    def unselect(self):
        self._is_selected = False

    def set_ui(self, ui):
        self._ui = ui
        
    def get_ui(self):
        return self._ui
        
    def add_button(self, button):
        self._buttons.append(button)
              
    def get_associated_buttons(self):
        return self._buttons
       
    def must_be_selected(self):
        mustbe = True
        for button in self._buttons:
            if not button.is_selected():
                mustbe =False
                break
        return mustbe
