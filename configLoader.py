import json
import sys
#sys.path.append(r'C:\Users\sylva\Documents\maya\2019\scripts\controllerSelector')
import customButton
reload(customButton)

class ConfigurationFileException(Exception):
    pass
    
class ConfigLoader():
    def __init__(self, filename):
        self._filename = filename
        self._buttons = []
        self._groups = []
        self._group_buttons = []
        self._tab_buttons = []
        self._tabs = {}
        self._colors = {}
        self._width = 0
        self._height = 0
        
    def parse(self):
        with open(self._filename) as f: # Opening configuration file
            tree = json.load(f) 
            # Closing file
            f.close()
            
        # Load width and height 
        width = tree['general']['width']
        height = tree['general']['height']
            
        if not isinstance(width, int):
            raise ConfigurationFileException("general.width must be an int")

        if not isinstance(height, int):
            raise ConfigurationFileException("general.height must be an int")

        if width <= 0:
            raise ConfigurationFileException("general.width must be positive")
            
        if height <= 0:
            raise ConfigurationFileException("general.height must be positive")

        self._width = width
        self._height = height
            
        # Loading colors dictionnary
        for color in tree['colors']:
            name = color['name']
            s_path = color['s_path']
            u_path = color['u_path']
                      
            if not isinstance(name, basestring):
                raise ConfigurationFileException("colors.color.name must be a string")
                
            if not isinstance(s_path, basestring):
                raise ConfigurationFileException("colors.color.s_path must be a string")
                
            if not isinstance(u_path, basestring):
                raise ConfigurationFileException("colors.color.u_path must be a string")

            self._colors[name] = [s_path, u_path]
        
        # Loading tabs list
        for tab in tree['tabs']:
            name = tab['name']
            background = tab['background']
                      
            if not isinstance(name, basestring):
                raise ConfigurationFileException("tabs.tab.name must be a string")
                
            if not isinstance(background, basestring):
                raise ConfigurationFileException("tabs.tab.background must be a string")
            
            self._tabs[name] = background
            b = customButton.TabButton(name)
            self._tab_buttons.append(b)

        
        # Load the list of group buttons
        for group_button in tree['group_buttons']:
            # Load attributes
            top_offset = group_button['top_offset'] 
            left_offset = group_button['left_offset'] 
            group = group_button['group']
            s_path = group_button['s_path']
            u_path = group_button['u_path']
            tab = group_button['tab']
            
            # Check button attributes type
            if not isinstance(top_offset, int):
                raise ConfigurationFileException("buttons.button.top_offset must be an integer")

            if not isinstance(left_offset, int):
                raise ConfigurationFileException("buttons.button.left_offset must be an integer")
                
            if not isinstance(group, basestring):
                raise ConfigurationFileException("group must be a string")

            if not isinstance(s_path, basestring):
                raise ConfigurationFileException("s_path must be a string")
            
            if not isinstance(u_path, basestring):
                raise ConfigurationFileException("u_path must be a string")
                
            if not isinstance(tab, basestring):
                raise ConfigurationFileException("buttons.button.tab must be a string")


            # Check attributes content              
            if top_offset < 0:
                raise ConfigurationFileException("buttons.button.top_offset must be positive or null")
                
            if left_offset < 0:
                raise ConfigurationFileException("buttons.button.left_offset must be positive or null")
                
            if tab not in self._tabs:
                raise ConfigurationFileException("buttons.button.tab : The tab must be defined first")

            b = customButton.GroupButton(group, top_offset, left_offset, s_path, u_path, tab)
            self._groups.append(group)
            self._group_buttons.append(b)
        
        # Finally, let's load the list of buttons
        for button in tree['buttons']:
            # Load attributes
            width = button['width'] 
            height = button['height'] 
            top_offset = button['top_offset'] 
            left_offset = button['left_offset'] 
            color = button['color']
            controller = button['controller']
            tab = button['tab']
            groups = []
            
            for group in button['groups']:
                if not isinstance(group, basestring):
                    raise ConfigurationFileException("button group must be a string")
                
                if group not in self._groups:
                    raise ConfigurationFileException("Group "+group+" does not exists. Create it first")
                    
                groups.append(group)
            
            # Check button attributes type
            if not isinstance(width, int):
                raise ConfigurationFileException("buttons.button.width must be an integer")
            
            if not isinstance(height, int):
                raise ConfigurationFileException("buttons.button.height must be an integer")

            if not isinstance(top_offset, int):
                raise ConfigurationFileException("buttons.button.top_offset must be an integer")

            if not isinstance(left_offset, int):
                raise ConfigurationFileException("buttons.button.left_offset must be an integer")
                
            if not isinstance(color, basestring):
                raise ConfigurationFileException("buttons.button.color must be a string")

            if not isinstance(controller, basestring):
                raise ConfigurationFileException("buttons.button.controller must be a string")
                
            if not isinstance(tab, basestring):
                raise ConfigurationFileException("buttons.button.tab must be a string")


            # Check attributes content
            if width <= 0:
                raise ConfigurationFileException("buttons.button.width must be positive")
                
            if height <= 0:
                raise ConfigurationFileException("buttons.button.height must be positive")
                
            if top_offset < 0:
                raise ConfigurationFileException("buttons.button.top_offset must be positive or null")
                
            if left_offset < 0:
                raise ConfigurationFileException("buttons.button.left_offset must be positive or null")
                
            if color not in self._colors:
                raise ConfigurationFileException("buttons.button.color : The color must be defined first")

            if tab not in self._tabs:
                raise ConfigurationFileException("buttons.button.tab : The tab must be defined first")


            b = customButton.Button(controller, width, height, top_offset, left_offset, self._colors[color][0], self._colors[color][1], tab, groups)
            self._buttons.append(b)

            
    @property
    def buttons(self):
        return self._buttons
        
    @property
    def group_buttons(self):
        return self._group_buttons
        
    @property
    def colors(self):
        return self._colors
        
    @property
    def tabs(self):
        return self._tabs
        
    @property
    def tab_buttons(self):
        return self._tab_buttons

    
    @property
    def width(self):
        return self._width
        
    @property
    def height(self):
        return self._height
        

        