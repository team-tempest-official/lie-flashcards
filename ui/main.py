from navdrawer import NavigationDrawer
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.animation import Animation
from kivy.uix.actionbar import ActionBar , ActionItem, ActionButton
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.utils import platform
from kivy.animation import Animation
from kivy.uix.dropdown import DropDown
from kivy.uix.widget import Widget
from kivy.uix.stencilview import StencilView
from kivy.uix.scrollview import ScrollView
from kivy.effects.scroll import ScrollEffect
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

from addcard import AddCard
from solomenu import SoloMenu
from study import Study
from presstextinput import PressTextInput
from tabtextinput import TabTextInput
from cardbrowser import CardBrowser
from gamemanager import GameManager
from playmenu import PlayMenu
from mainmenu import MainMenu
from deckmenu import DeckMenu
from playdeck import PlayDeck

Builder.load_file('screens/add_card.kv')
Builder.load_file('screens/deck_menu.kv')
Builder.load_file('screens/game_manager.kv')
Builder.load_file('screens/main_menu.kv')
Builder.load_file('screens/play_deck.kv')
Builder.load_file('screens/play_menu.kv')
Builder.load_file('screens/solo_menu.kv')
Builder.load_file('screens/study.kv')
Builder.load_file('screens/card_browser.kv')
Builder.load_file('modalviews/create_deck.kv')
Builder.load_file('modalviews/custom_modal_1.kv')
Builder.load_file('modalviews/custom_modal_2.kv')
Builder.load_file('modalviews/custom_modal_3.kv')
Builder.load_file('modalviews/custom_modal_4.kv')
Builder.load_file('modalviews/custom_modal_5.kv')

class ScrollBox(ScrollView):
    effect_cls = ScrollEffect


class ActionLabel(Label,ActionItem):
    pass


class ActionText(PressTextInput,ActionItem):
    pass


class SlideMenu(NavigationDrawer):
    def __init__(self, **kwargs):
        super(SlideMenu, self).__init__( **kwargs)


class TutorialApp(App):
    sm = ObjectProperty()
    history = ListProperty()
    prev = StringProperty()

    def build(self):
        self.sm = GameManager(transition=NoTransition())
        self.sm.switch_to_solo_menu()
        self.sm.ids.s3.ids.butd.text = self.sm.manager.implementation.decks[1].find_attribute("name").attribute_value_
        #self.sm.ids.s1.ids.b1.text = self.sm.manager.implementation.decks[1].find_attribute("name").attribute_value_
        self.history.append('main_menu')
        a = Screen()
        for a in self.sm.screens:
            a.bind(on_enter=self.record_history)
        self.bind(on_start=self.post_build_init)
        #Window.softinput_mode = 'pan'
        return self.sm

    def post_build_init(self, ev):
        if platform == 'android':
            import android
            android.map_key(android.KEYCODE_BACK, 1000)
            android.map_key(android.KEYCODE_MENU, 1001)
        win = self._app_window
        win.bind(on_keyboard=self._key_handler)

    def _key_handler(self, *args):
        key = args[1]
        if key in (1000, 27):
            if Window.keyboard_height is 0:
                if self.sm.modal_state is 1:
                    if len(self.history) == 1:
                        self.stop()
                    self.prev = self.history[len(self.history) - 2]
                    del self.history[-1]
                    self.sm.current = self.prev
                    return True
                else:
                    self.sm.modal_state.dismiss()
                    self.sm.modal_state = 1
            else:
                Window.release_all_keyboards()


    def record_history(self, *args, **kwargs):
        if self.prev != self.sm.current:
            self.history.append(self.sm.current)


if __name__ == "__main__":
    TutorialApp().run()
