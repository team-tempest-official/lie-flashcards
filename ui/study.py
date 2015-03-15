from navdrawer import NavigationDrawer
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.base import runTouchApp
from kivy.animation import Animation
from kivy.uix.scatter import Scatter
from kivy.uix.actionbar import ActionBar , ActionItem, ActionButton
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.utils import platform
from kivy.animation import Animation
from kivy.uix.dropdown import DropDown
from kivy.uix.modalview import ModalView
from kivy.uix.widget import Widget
from kivy.uix.stencilview import StencilView
from kivy.uix.scrollview import ScrollView
from kivy.effects.scroll import ScrollEffect
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.properties import (ObjectProperty, NumericProperty, OptionProperty, DictProperty,
                             BooleanProperty, StringProperty, ListProperty)
from kivy.resources import resource_add_path
from kivy.core.window import Window , Keyboard
import os.path
from storage.simple_implementation import SimpleImplementation
from storage.database_manager import DatabaseManager

from kivy.core.text.markup import MarkupLabel

from kivy.lang import Builder
import re

class Study(Screen):

    i = NumericProperty(1)

    def __init__(self, **kwargs):
        super(Study, self).__init__(**kwargs)

    def reset(self, *args):
        self.ids.bl_ans.clear_widgets()
        self.ids.bl_ans.add_widget(Button(text = "Show Answer",
                                            color = [0,0,0,1] ,
                                            background_normal =  '' ,
                                            background_color= [1,1,1,1] ,
                                            on_release = self.show_ans))
        self.ids.lab1.text = self.manager.current_deck.cards_[self.i].question_.find_attribute("question").attribute_value_
        self.ids.lab2.text = ''
        self.i += 1

    def show_ans(self, *args):
        self.ids.bl_ans.clear_widgets()
        self.ids.lab2.text = self.manager.current_deck.cards_[self.i - 1].answers_[0].find_attribute("answer").attribute_value_
        self.ids.bl_ans.add_widget(Button(text = "Hard",
                                          color = [0,0,0,1] ,
                                          background_normal =  '' ,
                                          background_color= [1,1,1,1] ,
                                          on_release = self.reset))
        self.ids.bl_ans.add_widget(Button(text = "Normal",
                                          color = [0,0,0,1] ,
                                          background_normal =  '' ,
                                          background_color= [1,1,1,1] ,
                                          on_release = self.reset))
        self.ids.bl_ans.add_widget(Button(text = "Easy",
                                          color = [0,0,0,1] ,
                                          background_normal =  '' ,
                                          background_color= [1,1,1,1] ,
                                          on_release = self.reset))
