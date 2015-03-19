from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionBar , ActionItem, ActionButton
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.modalview import ModalView
from kivy.uix.stencilview import StencilView
from kivy.uix.scrollview import ScrollView
from kivy.effects.scroll import ScrollEffect
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.properties import (ObjectProperty, NumericProperty, OptionProperty, DictProperty,
                             BooleanProperty, StringProperty, ListProperty)
from kivy.core.window import Window , Keyboard
from storage.simple_implementation import SimpleImplementation
from storage.database_manager import DatabaseManager


from createdeck import CreateDeck

class SoloMenu(Screen):

    #instance for createdeckmodalview
    create_deck_modalview = ObjectProperty()

    #method to create 'create deck' modalview
    def show_createdeck(self):
        self.create_deck_modalview = CreateDeck()
        self.create_deck_modalview.ids.but1.bind(on_release = self.create_deck)
        self.create_deck_modalview.open()
        self.manager.modal_state = self.create_deck_modalview

    #method to create a new deck 
    def create_deck(self , *args):
        #create a new deck in memory
        name = self.manager.manager.create_attribute("name","string",self.create_deck_modalview.ids.deck_txt.text)
        nr_of_cards = self.manager.manager.create_attribute("nr_of_cards" , "number" , 0)
        nr_of_cards_studied = self.manager.manager.create_attribute("nr_of_cards_studied" , "number" , 0)
        nr_of_cards_to_study = self.manager.manager.create_attribute("nr_of_cards_to_study" , "number" , 0)
        deck = self.manager.manager.create_deck([],[name, nr_of_cards ,  ])
        self.manager.manager.add_deck(deck)

        #create a button for our new deck
        btn = Button(color = (0,0,0,1),
                    text = deck.find_attribute("name").attribute_value_,
                    size_hint_y = None,
                    height = '50dp',
                    background_normal = '',
                    background_color = (1,1,1,1),
                    on_release = self.manager.switch_to_deckplay)
        self.ids.gl1.add_widget(btn)
        self.manager.modal_state = 1

    #method to switch to AddCard
    def switch_to_addcard(self, *args):
        self.manager.current = 'add_card'
