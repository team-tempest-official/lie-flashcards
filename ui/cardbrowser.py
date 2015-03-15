from navdrawer import NavigationDrawer
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.base import runTouchApp
from kivy.animation import Animation
from kivy.uix.actionbar import ActionBar , ActionItem, ActionButton
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.animation import Animation
from kivy.uix.dropdown import DropDown
from kivy.uix.widget import Widget
from kivy.uix.stencilview import StencilView
from kivy.uix.scrollview import ScrollView
from kivy.effects.scroll import ScrollEffect
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.properties import (ObjectProperty, NumericProperty, OptionProperty, DictProperty,
                             BooleanProperty, StringProperty, ListProperty)
from kivy.core.window import Window , Keyboard

from storage.simple_implementation import SimpleImplementation
from storage.database_manager import DatabaseManager

from kivy.core.text.markup import MarkupLabel
from presstextinput import PressTextInput

class ActionText(PressTextInput,ActionItem):
    pass

class CardBrowser(Screen):

    sb = ObjectProperty()
    sinput = ObjectProperty()
    junk = ObjectProperty()

    def start_search(self, *args):
        self.ids.av.remove_widget(self.ids.av.children[0])
        self.sinput = ActionText(font_size = 25, padding_y = [10,0])
        self.sinput.multiline = False
        self.sb = ActionButton (text = 'X',on_release = self.close)
        self.sinput.my_button = self.sb
        self.ids.av.add_widget(self.sinput)
        self.ids.av.add_widget(self.sb)
        self.sb.bind(state = self.please_search)

    def close(self, *args):
        self.ids.av.remove_widget(self.sinput)
        self.ids.av.remove_widget(self.sb)
        self.ids.av.add_widget(ActionButton(text = 'Search' , on_release = self.start_search))

    def please_search(self, *args):
        if self.sb.state is 'down' :
            self.manager.cb_display_cards('search' , self.manager.mainbutton , self.sinput.text)
            self.sb.state = 'normal'
