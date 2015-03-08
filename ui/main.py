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

class TabTextInput(TextInput):

    ok = NumericProperty(0)
    ko = NumericProperty(0)
    test = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        super(TabTextInput, self).__init__(*args, **kwargs)

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        key, key_str = keycode
        if key is not 8:
            if key is 13 or self.cursor_col == 20:
                self.test += 1
                self.insert_text('\n')
                self.add_line()
                return False
        else:
            if self.cursor_col==0 and self.cursor_row>0:
                self.remove_line()
        return super(TabTextInput, self).keyboard_on_key_down(window, keycode, text, modifiers)

    def add_line(self):
        self.height += self.line_height
        self.ok += 1
        #self.y -= self.line_height

    def remove_line(self):
        self.height -= self.line_height
        self.ko += 1
        #self.y += self.line_height

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

    def switch_to_deckplay(self , button ):
        self.ids.s6.ids.deck_label.text = button.text
        self.ids.s6.ids.action_deck_label.text = button.text
        self.current = 'play_deck'


class MainMenu(Screen):
    pass
    
    
class PlayMenu(Screen):
    pass


class SoloMenu(Screen):
    
    deck_nr = NumericProperty(1)
    b = ObjectProperty()
    create_deck_modalview = ObjectProperty()
    curr_y = NumericProperty('476dp')

    def show_createdeck(self):
        self.create_deck_modalview = CreateDeck()
        self.create_deck_modalview.ids.but1.bind(on_release = self.create_deck)
        self.create_deck_modalview.open()

    def create_deck(self , *args):
        self.curr_y -=self.ids.b1.height * 3/2
        self.b = Button( id = 'b'+str(self.deck_nr+1) ,
                    text = self.create_deck_modalview.ids.deck_txt.text ,
                    x = self.ids.fl1.x ,
                    size_hint_y = None ,
                    height = '50dp' ,
                    y = self.curr_y , #self.ids['b'+str(self.deck_nr)].y - self.ids['b'+str(self.deck_nr)].height * 3/2  ,
                    color = [0,0,0,1] ,
                    text_size = (self.width * 3/4 , None) ,
                    background_normal = '' ,
                    background_color = [1,1,1,1] ,
                    on_release = self.manager.switch_to_deckplay)
        self.deck_nr+=1
        self.ids.fl1.add_widget(self.b)

    
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
        self.sm = GameManager(transition=NoTransition())
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

