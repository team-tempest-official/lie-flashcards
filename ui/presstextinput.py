from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty


class PressTextInput(TextInput):

    my_button = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(PressTextInput, self).__init__(*args, **kwargs)

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        key, key_str = keycode
        #checking if the user presses enter
        if key is 13:
            #switch the state of the chosen button
            self.my_button.state = 'down'
            return False
        return super(PressTextInput, self).keyboard_on_key_down(window, keycode, text, modifiers)

