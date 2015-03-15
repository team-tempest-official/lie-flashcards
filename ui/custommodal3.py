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

class CustomModal3(ModalView):
    num = NumericProperty(0)
    
    def __init__(self, height, **kwargs):
        super(CustomModal3, self).__init__(**kwargs)
        self.num = height
