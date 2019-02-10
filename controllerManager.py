class ControllerManager():
    def __init__(self, buttons, group_buttons, tabs):
        self._buttons = buttons
        self._group_buttons = group_buttons
        self._selection_list = []
        self._tab_buttons = tabs
        self.__associate_buttons_to_group_buttons()
        self.__associate_buttons_to_tab_buttons()
        
    def __associate_buttons_to_group_buttons(self):
        for group_button in self._group_buttons:
            for button in self._buttons:
                if group_button.group in button.groups:
                    group_button.add_button(button)
        
        
    def __associate_buttons_to_tab_buttons(self):
        for tab_button in self._tab_buttons:
            for button in self._buttons:
                if tab_button.name == button.tab:
                    tab_button.add_button(button)

    def get_button_by_controller(self, controller):
        button = None
        for b in self._buttons:
            if b.controller == controller:
                button = b
                break
        return button
        
    def add_controller_to_selection(self, object_name):
        """
            Check if the object is a referenced controller from the animPicker.
            If exists, let's add it to the selected_list
        """
        for button in self._buttons:
            if object_name == button.controller:
                if button.controller not in self._selection_list:
                    self._selection_list.append(button.controller)
                    break
                    
    def change_selected_controller(self, object_name):
        """
            Check if the object is a referenced controller from the animPicker.
            If exists, let's add it to the selected_list
        """
        self.clear_selection()
        for button in self._buttons:
            if object_name == button.controller:
                self._selection_list.append(button.controller)
                break

                    
    def remove_controller_from_selection(self, object_name):
        """
            Check if the object is in the selection list.
            If exists, we have to remove it from the selection list
        """
        if object_name in self._selection_list:
            self._selection_list.remove(object_name)
            
    def clear_selection(self):
        self._selection_list = []

                    
    def get_selection_list(self):
        return self._selection_list
        
    def is_button_unique(self, button):
        currentlist = self._selection_list
        unique = False
        if len(currentlist) > 0:
            if button.controller in currentlist:
                currentlist.remove(button.controller)
            if len(currentlist) == 0:
                unique = True
        return unique

        
    def is_buttongroup_unique(self, group_button):
        currentlist = self._selection_list
        unique = False
        if len(currentlist) > 0:
            for button in group_button.get_associated_buttons():
                if button.controller in currentlist:
                    currentlist.remove(button.controller)
            if len(currentlist) == 0:
                unique = True
        return unique
               
        
    @property
    def buttons(self):
        return self._buttons
        
    @property
    def group_buttons(self):
        return self._group_buttons    
    
    @property
    def tab_buttons(self):
        return self._tab_buttons