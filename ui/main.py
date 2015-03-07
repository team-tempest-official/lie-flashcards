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
from kivy.uix.actionbar import ActionBar , ActionItem
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.utils import platform
from kivy.animation import Animation
from kivy.uix.modalview import ModalView
from kivy.uix.widget import Widget
from kivy.uix.stencilview import StencilView
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.properties import (ObjectProperty, NumericProperty, OptionProperty, DictProperty,
                             BooleanProperty, StringProperty, ListProperty)
from kivy.resources import resource_add_path
import os.path


class CustomModal1(ModalView):
    pass
    
    
class CustomModal2(ModalView):
    pass


class CreateDeck(ModalView):
	pass


class AddCard(Screen):
    ids_ch = ['ch1', 'ch2', 'ch3']
    index = 0
    modal = ObjectProperty(None)

    def show_modal1(self):
        self.modal = CustomModal1()
        self.modal.ids[self.ids_ch[self.index]].active = True
        self.modal.ids.bu1.fast_bind('on_release', self.chg_text, self.modal.ids.bu1.text,1)
        self.modal.ids.bu2.fast_bind('on_release', self.chg_text, self.modal.ids.bu2.text,2)
        self.modal.ids.bu3.fast_bind('on_release', self.chg_text, self.modal.ids.bu3.text,3)
        self.modal.ids.ch1.fast_bind('active', self.chg_text, self.modal.ids.bu1.text,1)
        self.modal.ids.ch2.fast_bind('active', self.chg_text, self.modal.ids.bu2.text,2)
        self.modal.ids.ch3.fast_bind('active', self.chg_text, self.modal.ids.bu3.text,3)
        self.modal.open()
        
        
        
    def show_modal2(self):
        self.modal = CustomModal2()
        self.modal.ids.cm1.fast_bind('on_release', self.chg_text,self.modal.ids.cm1.text,0)
        self.modal.open()
          
        
    def chg_text(self, *args):
        if args[1]:
            self.index = args[1] - 1
            self.ids.butp.text = args[0]
        else:
            self.ids.butd.text = args[0]

class GameManager(ScreenManager):
    pass


class MainMenu(Screen):
    pass
    
    
class PlayMenu(Screen):
    pass


class SoloMenu(Screen):
    def show_createdeck(self):
        modal = CreateDeck()
        modal.open()
    
    
class DeckMenu(Screen):
    pass
    

class PlayDeck(Screen):
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

