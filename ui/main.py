from navdrawer import NavigationDrawer
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.animation import Animation
from kivy.uix.scatter import Scatter
from kivy.uix.actionbar import ActionBar , ActionItem
from kivy.uix.actionbar import ActionBar
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.utils import platform
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.uix.stencilview import StencilView
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.properties import (ObjectProperty, NumericProperty, OptionProperty,
                             BooleanProperty, StringProperty, ListProperty)
from kivy.resources import resource_add_path
import os.path


class GameManager(ScreenManager):
    pass


class MainMenu(Screen):
    pass
    
    
class PlayMenu(Screen):
    pass


class SoloMenu(Screen):
    pass
    
    
class DeckMenu(Screen):
    pass
    

class ActionLabel(Label,ActionItem):
	pass
    
    
class SlideMenu(NavigationDrawer):
    def __init__(self, **kwargs):
        super(SlideMenu, self).__init__( **kwargs)
    
class TutorialApp(App):
    sm = ObjectProperty()
    history = ListProperty()    
    prev = StringProperty()

    def build(self):
        self.sm = ScreenManager(transition=NoTransition())
        self.history.append('main_menu')
        a = Screen()
        for a in self.sm.screens:
            a.bind(on_enter=self.record_history)
        self.bind(on_start=self.post_build_init)
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
            if len(self.history) == 1:
                self.stop()
            self.prev = self.history[len(self.history) - 2]
            del self.history[-1]
            self.sm.current = self.prev
            return True


    def record_history(self, *args, **kwargs):
        if self.prev != self.sm.current:
            self.history.append(self.sm.current)
        

if __name__ == "__main__":
    TutorialApp().run()

