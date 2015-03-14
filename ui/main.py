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

class PressTextInput(TextInput):

    my_button = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(PressTextInput, self).__init__(*args, **kwargs)

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        key, key_str = keycode
        if key is 13:
            self.my_button.state = 'down'
            print 'castane'
            return False
        return super(PressTextInput, self).keyboard_on_key_down(window, keycode, text, modifiers)

class TabTextInput(TextInput):

    ok = NumericProperty(0)
    ko = NumericProperty(0)
    test = NumericProperty(0)
    test1 = NumericProperty(0)
    counter = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        super(TabTextInput, self).__init__(*args, **kwargs)

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        key, key_str = keycode
        if key is not 8:
            if self.cursor_offset() >  self.width - self.width * 6/100 :
                self.insert_text('\n')
                return False
        return super(TabTextInput, self).keyboard_on_key_down(window, keycode, text, modifiers)

    def add_line(self):
        self.height += self.line_height
        self.test+=1
        self.test1+=1
        self.counter +=1
        self.ok += 1
        #self.y -= self.line_height

    def remove_line(self):
        self.height -= self.line_height
        self.ko += 1
        self.counter -=1
        #self.y += self.line_height

class CustomModal1(ModalView):
    pass

class CustomModal2(ModalView):

    mn = ObjectProperty(None)
    scrn = ObjectProperty(None)

    def __init__(self, man, screen, **kwargs):
        super(CustomModal2, self).__init__(**kwargs)
        self.mn = man
        self.scrn = screen

        for d in self.mn.implementation.decks:
            if d is not self.mn.implementation.decks[0]:
                b = Button(text = d.find_attribute("name").attribute_value_ ,
                            background_normal = '' ,
                            color = [0,0,0,1] ,
                            background_color = [1,1,1,1] ,
                            on_release = self.scrn.chg_text_md2 )
                self.ids.gl1.height += b.height / 2
                if self.height < 300:
                    self.height += b.height / 2
                self.ids.gl1.add_widget(b)
                print self.height

class CustomModal3(ModalView):
    pass

class CustomModal4(ModalView):
    pass

class CustomModal5(ModalView):
    pass

class CreateDeck(ModalView):
    pass

class AddCard(Screen):
    ids_ch = ['ch1', 'ch2', 'ch3']
    index = 0
    modal = ObjectProperty(None)
    man = ObjectProperty(None)
    q = ObjectProperty(None)
    a = ObjectProperty(None)
    ok_q = BooleanProperty(False)
    ok_a = BooleanProperty(False)

    def __init__(self, **kwargs):
        return super(AddCard, self).__init__(**kwargs)

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
        self.modal = CustomModal2(self.manager.manager,self)
        #self.modal.ids.cm1.text = self.manager.manager.implementation.decks[0].find_attribute("name").attribute_value_
        #self.modal.ids.cm1.fast_bind('on_release', self.chg_text,self.modal.ids.cm1.text,0)
        self.modal.open()


##TODO:
    """ Add focus true on textinput when the modalview pops """
    def show_modal3(self):
        self.modal = CustomModal3()
        self.modal.ids.done.bind(on_release = self.done1)
        # 'Add answer' button binded to answer method
        self.modal.ids.answer.bind(on_release = self.answer)
        self.modal.open()

    # method for releasing 'Add answer' button to send the user directly to add answer modalview
    def answer(self, b):
        self.done1()
        self.show_modal4()

    def show_modal4(self):
        self.modal = CustomModal4()
        self.modal.ids.done.bind(on_release = self.done2)
        self.modal.ids.create_card.bind(on_release = self.create_card)
        self.modal.open()

    def done1(self, *args):
        if self.modal.ids.tit.text is not '':
            self.ids.lab_q.text = self.modal.ids.tit.text
            self.q = self.manager.manager.create_attribute("question","string",self.ids.lab_q.text)
            self.ok_q = True

    def done2(self, *args):
        if self.modal.ids.tit.text is not '':
            self.ids.lab_a.text = self.modal.ids.tit.text
            self.a = self.manager.manager.create_attribute("answer","string",self.ids.lab_a.text)
            self.ok_a = True

##TODO:
        """ Add Question/Answer should turn into Edit Question/Answer and
            the text enter previously should be found in the TextInput """

    def ac_create_card(self):
        if self.ok_q and self.ok_a:
            ans = self.manager.manager.create_qa([self.a, ])
            que = self.manager.manager.create_qa([self.q, ])
            card = self.manager.manager.create_card(que,[ans, ],[])
            print 'Card %r created' % card
            self.manager.manager.find_deck_by_attribute("name",self.ids.butd.text)[0].cards_.append(card)
            self.manager.manager.implementation.decks[0].cards_.append(card)
            self.ok_q = False
            self.ok_a = False
            self.ids.lab_a.text = ''
            self.ids.lab_q.text = ''
        elif self.ok_q is False:
            print 'Please add question'
        elif self.ok_a is False:
            print 'Please add answer'

    def create_card(self, *args):
        self.done2()
        if self.ok_a and self.ok_q:
            ans = self.manager.manager.create_qa([self.a, ])
            que = self.manager.manager.create_qa([self.q, ])
            card = self.manager.manager.create_card(que,[ans, ],[])
            print 'Card %r created' % card


    ## [0] must be removed when find_deck_by_attributes will be fixed
            self.manager.manager.find_deck_by_attribute("name",self.ids.butd.text)[0].cards_.append(card)
            self.manager.manager.implementation.decks[0].cards_.append(card)
            #print self.manager.manager.find_deck_by_attribute("name",self.ids.butd.text)[0].cards_

            self.ok_q = False
            self.ok_a = False
            self.ids.lab_a.text = ''
            self.ids.lab_q.text = ''
        elif self.ok_q is False:
            print 'Please add question'
        elif self.ok_a is False:
            print 'Please add answer'

    def show_modal5(self):
        self.modal = CustomModal5()
        self.modal.open()

##TODO:
        """ Create Tags functionality , basicaly add an attribute to card +
            bind the button from the CustomModal5"""

    def chg_text_md2(self, b):
        self.ids.butd.text = b.text
        self.modal.dismiss()

    def chg_text(self, *args):
        if args[1]:
            self.index = args[1] - 1
            self.ids.butp.text = args[0]
        else:
            self.ids.butd.text = args[0]

class GameManager(ScreenManager):

    current_deck = ObjectProperty(None)

    ## mainbutton nu are rost aici , trebuie implementat altfel !

    mainbutton = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(GameManager, self).__init__(**kwargs)
        self.manager = DatabaseManager(SimpleImplementation())

        name = self.manager.create_attribute("name","string","All Cards")
        deck = self.manager.create_deck([],[name, ])
        self.manager.add_deck(deck)

        self.manager.generate_data()
        for card in self.manager.implementation.decks[1].cards_:
            self.manager.implementation.decks[0].cards_.append(card)


    def prepare(self, text):
        self.current_deck = self.manager.find_deck_by_attribute("name",text)[0]
        self.ids.s7.i = 0
        self.ids.s7.ids.stal.text = 'Study ' + text
        self.ids.s7.reset()
        self.current = 'study'

    def switch_to_deckplay(self , button ):
        self.ids.s6.ids.deck_label.text = button.text
        self.ids.s6.ids.action_deck_label.text = button.text
        self.current = 'play_deck'

    def set_deck(self,text):
        self.ids.s3.ids.butd.text = text
        self.current = 'add_card'


    def switch_to_card_browser(self):
        self.current = 'card_browser'

        dropdown = DropDown()
        self.ids.s8.ids.ddbox.clear_widgets()


        #self.ids.s8.ids.ddbox.add_widget(dropdown)
        self.mainbutton = Button(text = 'All Cards',
                                 color = [0,0,0,1] ,
                                 background_color = [1,1,1,1] ,
                                 background_normal = '' )
        self.ids.s8.ids.ddbox.add_widget(self.mainbutton)
        self.mainbutton.fast_bind('on_release' ,dropdown.open)


        for decks in self.manager.implementation.decks:
            btn = Button(text = decks.find_attribute("name").attribute_value_, size_hint_y = None, height = '48dp',
                         color = [0,0,0,1] ,
                         background_color = [1,1,1,1] ,
                         background_normal = '' )
            btn.fast_bind('on_release', self.dd_select,btn,dropdown)
            dropdown.add_widget(btn)

        dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))

        self.cb_display_cards('basic',self.mainbutton)

    def dd_select(self, *args):
        args[1].select(args[0].text)
        self.cb_display_cards('basic',args[0])

    def cb_display_cards(self, *args):

 ## TODO:
        """ Add search bar in the ActionBar by inheriting it from ActionItem """


 ## BUG:
        """ Find a way to cancel re.search() special regex characters . We want it to look
            only normal """

 ## TODO:
        """ Add better implementation of this """


        self.ids.s8.ids.gl.clear_widgets()
        self.ids.s8.ids.search.state = 'normal'
        if args[0] is 'basic':

            for card in self.manager.find_deck_by_attribute("name",args[1].text)[0].cards_:#find_deck_by_attribute("name",args[1].text)[0].cards_:
                self.ids.s8.ids.gl.add_widget(Button(size_hint_y = None,
                                                     height = '35dp',
                                                     text = card.question_.find_attribute("question").attribute_value_ ,#.replace(args[2],'[color=#FF0000]%s[/color]' % args[2]) ,
                                                     color = [0,0,0,1] ,
                                                     background_color = [1,1,1,1] ,
                                                     background_normal = '' ,
                                                     background_down = ''))

                self.ids.s8.ids.gl.add_widget(Button(size_hint_y = None,
                                                     height = '35dp',
                                                     text = card.answers_[0].find_attribute("answer").attribute_value_ ,#.replace(args[2],'[color=#FF0000]%s[/color]' % args[2]) ,
                                                     color = [0,0,0,1] ,
                                                     background_color = [1,1,1,1] ,
                                                     background_normal = '' ,
                                                     background_down = ''))
        elif args[0] is 'search':

            for card in self.manager.find_deck_by_attribute("name",args[1].text)[0].cards_:#find_deck_by_attribute("name",args[1].text)[0].cards_:
                if args[2] in card.question_.find_attribute("question").attribute_value_ or \
                    args[2] in card.answers_[0].find_attribute("answer").attribute_value_:
                    self.ids.s8.ids.gl.add_widget(Button(size_hint_y = None,
                                                         markup = True ,
                                                         height = '35dp',
                                                         color = [0,0,0,1] ,
                                                         text = card.question_.find_attribute("question").attribute_value_ ,#.replace(args[2],'[color=#FF0000]%s[/color]' % args[2]) ,
                                                         background_color = [1,1,1,1] ,
                                                         background_normal = '' ,
                                                         background_down = '' ))

                    self.ids.s8.ids.gl.add_widget(Button(size_hint_y = None,
                                                         markup = True ,
                                                         height = '35dp',
                                                         color = [0,0,0,1] ,
                                                         text = card.answers_[0].find_attribute("answer").attribute_value_ ,#.replace(args[2],'[color=#FF0000]%s[/color]' % args[2]) ,
                                                         background_color = [1,1,1,1] ,
                                                         background_normal = '' ,
                                                         background_down = ''))
class MainMenu(Screen):
    pass


class PlayMenu(Screen):
    pass


class ActionBL(BoxLayout, ActionItem):
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
        print self.ids.av.children
        self.ids.av.remove_widget(self.sinput)
        self.ids.av.remove_widget(self.sb)
        self.ids.av.add_widget(ActionButton(text = 'Search' , on_release = self.start_search))

    def please_search(self, *args):
        if self.sb.state is 'down' :
            self.manager.cb_display_cards('search' , self.manager.mainbutton , self.sinput.text)
            self.sb.state = 'normal'

class SoloMenu(Screen):

    buttons = ListProperty([])
    deck_nr = NumericProperty(1)
    copy_deck_nr = NumericProperty(1)
    b = ObjectProperty()
    create_deck_modalview = ObjectProperty()
    curr_y = NumericProperty()
    once = True

    def show_createdeck(self):
        self.create_deck_modalview = CreateDeck()
        self.create_deck_modalview.ids.but1.bind(on_release = self.create_deck)
        self.create_deck_modalview.open()

    def create_deck(self , *args):

        name = self.manager.manager.create_attribute("name","string",self.create_deck_modalview.ids.deck_txt.text)
        deck = self.manager.manager.create_deck([],[name, ])
        self.manager.manager.add_deck(deck)

        if self.once:
            self.buttons.append(self.ids.b1)
            self.once = False
        if self.buttons[-1].y < self.ids.b1.height * 3/2 :
            self.ids.bl.height += self.ids.b1.height *3/2
            self.ids.fl1.height += self.ids.b1.height * 3/2
            for btn in self.buttons:
                btn.y += self.ids.b1.height * 3/2
        self.b = Button( text = self.create_deck_modalview.ids.deck_txt.text ,
                    x = self.ids.fl1.x ,
                    size_hint_y = None ,
                    height = '50dp' ,
                    y = self.buttons[-1].y - self.buttons[-1].height * 3/2,
                    color = [0,0,0,1] ,
                    text_size = (self.width * 3/4 , None) ,
                    background_normal = '' ,
                    background_color = [1,1,1,1] ,
                    on_release = self.manager.switch_to_deckplay)
        self.deck_nr+=1
        self.b.id = 'b'+str(self.deck_nr)
        self.buttons.append(self.b)
        self.ids.fl1.add_widget(self.b)


class DeckMenu(Screen):
    pass


class PlayDeck(Screen):
    pass

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
        self.sm.ids.s3.ids.butd.text = self.sm.manager.implementation.decks[1].find_attribute("name").attribute_value_
        self.sm.ids.s1.ids.b1.text = self.sm.manager.implementation.decks[1].find_attribute("name").attribute_value_
        self.history.append('main_menu')
        a = Screen()
        print self.sm.screens
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
