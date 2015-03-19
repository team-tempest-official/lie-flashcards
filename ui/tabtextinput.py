from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty


class TabTextInput(TextInput):

    my_button = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(TabTextInput, self).__init__(*args, **kwargs)

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        key, key_str = keycode
        #checking if the user presses enter
        if key is 13:
             #activate chosen's button on_release event
             self.my_button.dispatch("on_release")
             return False
        return super(TabTextInput, self).keyboard_on_key_down(window, keycode, text, modifiers)

    
