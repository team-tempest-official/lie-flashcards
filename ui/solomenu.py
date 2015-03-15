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
from kivy.core.window import Window , Keyboard
from storage.simple_implementation import SimpleImplementation
from storage.database_manager import DatabaseManager


from createdeck import CreateDeck

class SoloMenu(Screen):

    buttons = ListProperty([])
    b = ObjectProperty()
    create_deck_modalview = ObjectProperty()


    def show_createdeck(self):
        self.create_deck_modalview = CreateDeck()
        self.create_deck_modalview.ids.but1.bind(on_release = self.create_deck)
        self.create_deck_modalview.open()
        self.manager.modal_state = self.create_deck_modalview

    def create_deck(self , *args):

        name = self.manager.manager.create_attribute("name","string",self.create_deck_modalview.ids.deck_txt.text)
        deck = self.manager.manager.create_deck([],[name, ])
        self.manager.manager.add_deck(deck)

        btn = Button(color = (0,0,0,1),
                    text = deck.find_attribute("name").attribute_value_,
                    size_hint_y = None,
                    height = '50dp',
                    background_normal = '',
                    background_color = (1,1,1,1),
                    on_release = self.manager.switch_to_deckplay)
        self.ids.gl1.add_widget(btn)
        self.manager.modal_state = 1

