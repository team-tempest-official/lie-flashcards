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
from kivy.uix.checkbox import CheckBox
from kivy.metrics import dp
from kivy.properties import (ObjectProperty, NumericProperty, OptionProperty, DictProperty,
                             BooleanProperty, StringProperty, ListProperty)
from storage.simple_implementation import SimpleImplementation
from storage.database_manager import DatabaseManager

from kivy.core.window import Window , Keyboard

from custommodal1 import CustomModal1
from custommodal2 import CustomModal2
from custommodal3 import CustomModal3
from custommodal4 import CustomModal4
from custommodal5 import CustomModal5


class AddCard(Screen):
    ids_ch = ['ch1', 'ch2', 'ch3']
    index = 0
    
    #variable to cycle modalviews
    modal = ObjectProperty(None)

    man = ObjectProperty(None)
    q = ObjectProperty(None)
    a = ObjectProperty(None)
    ok_q = BooleanProperty(False)
    ok_a = BooleanProperty(False)

    #variable to track the current card
    current_card = ObjectProperty(None)

    def __init__(self, **kwargs):
        return super(AddCard, self).__init__(**kwargs)

    #method to display the cardtype modalview
    #all the modalview dismisses are done in add_card.kv
    def show_modal1(self):
        self.modal = CustomModal1()
        self.manager.modal_state = self.modal
        #defaulting the current type checkbox to be active when the modalview pops
        self.modal.ids[self.ids_ch[self.index]].active = True
        #binding all our buttons and checkboxes to our methods
        self.modal.ids.bu1.fast_bind('on_release', self.chg_text, self.modal.ids.bu1.text,1)
        self.modal.ids.bu2.fast_bind('on_release', self.chg_text, self.modal.ids.bu2.text,2)
        self.modal.ids.bu3.fast_bind('on_release', self.chg_text, self.modal.ids.bu3.text,3)
        self.modal.ids.ch1.fast_bind('active', self.chg_text, self.modal.ids.bu1.text,1)
        self.modal.ids.ch2.fast_bind('active', self.chg_text, self.modal.ids.bu2.text,2)
        self.modal.ids.ch3.fast_bind('active', self.chg_text, self.modal.ids.bu3.text,3)
        self.modal.open()

    #method to display the deck selecter modalview
    def show_modal2(self):
        #creating the modalview passing the storage manager and the AddCard screen to the custommodal2's __init__ method 
        self.modal = CustomModal2(self.manager.manager,self)
        self.manager.modal_state = self.modal
        self.modal.open()

    #method to move the currently displayed modalview in case the keyboard will cover it
    def move(self, *args):
        print 'bb'
        if self.modal.ids.tit.focus is True and Window.keyboard_height is not 0:
            self.modal.pos_hint = {'left': .8, 'top': (Window.keyboard_height + self.modal.height) / self.height}
        else:
            self.modal.pos_hint = {'left': .8, 'top': .9}


##TODO:
    """ Add focus true on textinput when the modalview pops """
    #method to display the add question modalview
    def show_modal3(self):
        self.modal = CustomModal3()
        self.manager.modal_state = self.modal
        #binding the buttons
        self.modal.ids.done.bind(on_release = self.done1)
        self.modal.ids.answer.bind(on_release = self.answer)
        #checking if the keyboard is displayed by binding its height
        Window.bind(keyboard_height = self.move)
        #defaulting the displayed text to what we previously had in question
        self.modal.ids.tit.text = self.ids.lab_q.text
        self.modal.open()

    # method for releasing 'Add answer' button to send the user directly to add answer modalview
    def answer(self, b):
        self.done1()
        self.show_modal4()

    #method to display the add answer modalview
    def show_modal4(self):
        self.modal = CustomModal4()
        self.manager.modal_state = self.modal
        self.modal.ids.done.bind(on_release = self.done2)
        self.modal.ids.create_card.bind(on_release = self.create_card)
        Window.bind(keyboard_height = self.move)
        self.modal.ids.tit.text = self.ids.lab_a.text
        #switching the text of the 'create card' button to 'save changes' button when the 'create card' button from AddCard's actionbar switches 
        self.modal.ids.create_card.text = self.ids.ac_create_card.text
        self.modal.open()

    #method to close the addquestion modalview
    def done1(self, *args):
        if self.modal.ids.tit.text is not '':
            self.ids.lab_q.text = self.modal.ids.tit.text
            self.q = self.manager.manager.create_attribute("question","string",self.ids.lab_q.text)
            self.ok_q = True
            self.manager.modal_state = 1

    #method to close the addanswer modalview
    def done2(self, *args):
        if self.modal.ids.tit.text is not '':
            self.ids.lab_a.text = self.modal.ids.tit.text
            self.a = self.manager.manager.create_attribute("answer","string",self.ids.lab_a.text)
            self.ok_a = True
            self.manager.modal_state = 1

##TODO:
        """ Add Question/Answer should turn into Edit Question/Answer and
            the text enter previously should be found in the TextInput """

    #method that creates the card from the button on the actionbar 
    def ac_create_card(self):
        #cehcking if the button is 'create card' or 'save changes'
        if self.ids.ac_create_card.text == 'Create card':
            if self.ok_q and self.ok_a:
                ans = self.manager.manager.create_qa([self.a, ])
                que = self.manager.manager.create_qa([self.q, ])
                tags = self.manager.manager.create_attribute ("tags" , "string" , self.ids.tags_label.text)
                card = self.manager.manager.create_card(que,[ans, ],[tags, ])
                print 'Card %r created' % card
                self.manager.manager.find_deck_by_attribute("name",self.ids.butd.text)[0].cards_.append(card)
                self.manager.manager.implementation.decks[0].cards_.append(card)
                self.manager.manager.find_deck_by_attribute("name",self.ids.butd.text)[0].find_attribute("nr_of_cards").attribute_value_ = int(self.manager.manager.find_deck_by_attribute("name",self.ids.butd.text)[0].find_attribute("nr_of_cards").attribute_value_) + 1
                self.ok_q = False
                self.ok_a = False
                self.ids.lab_a.text = ''
                self.ids.lab_q.text = ''
            elif self.ok_q is False:
                print 'Please add question'
            elif self.ok_a is False:
                print 'Please add answer'
        else:
            self.current_card.question_.find_attribute("question").attribute_value_ = self.ids.lab_q.text
            self.current_card.answers_[0].find_attribute("answer").attribute_value_ = self.ids.lab_a.text
            self.current_card.find_attribute("tags").attribute_value_ = self.ids.tags_label.text
            self.manager.switch_to_card_browser()



    #methid that creates the card from the addanswer modalview
    def create_card(self, *args):
        #saving our answer first since we didnt had the chance
        self.done2()
        #cehcking if the button is 'create card' or 'save changes'
        if self.ids.ac_create_card.text == 'Create card':
            if self.ok_a and self.ok_q:
                ans = self.manager.manager.create_qa([self.a, ])
                que = self.manager.manager.create_qa([self.q, ])
                tags = self.manager.manager.create_attribute ("tags" , "string" , self.ids.tags_label.text)
                card = self.manager.manager.create_card(que,[ans, ],[tags, ])
                print 'Card %r created' % card
                self.manager.modal_state = 1


                self.manager.manager.find_deck_by_attribute("name",self.ids.butd.text)[0].cards_.append(card)
                self.manager.manager.implementation.decks[0].cards_.append(card)
                self.manager.manager.find_deck_by_attribute("name",self.ids.butd.text)[0].find_attribute("nr_of_cards").attribute_value_ = int(self.manager.manager.find_deck_by_attribute("name",self.ids.butd.text)[0].find_attribute("nr_of_cards").attribute_value_) + 1

                self.ok_q = False
                self.ok_a = False
                self.ids.lab_a.text = ''
                self.ids.lab_q.text = ''
            elif self.ok_q is False:
                print 'Please add question'
            elif self.ok_a is False:
                print 'Please add answer'
        else:
            #code for 'save changes' just making sure we save the changes before we switch back to cardbrowser
            self.current_card.question_.find_attribute("question").attribute_value_ = self.ids.lab_q.text
            self.current_card.answers_[0].find_attribute("answer").attribute_value_ = self.ids.lab_a.text
            self.current_card.find_attribute("tags").attribute_value_ = self.ids.tags_label.text
            self.manager.switch_to_card_browser()

    #method for the tags modalview
    def show_modal5(self):
        self.modal = CustomModal5()
        self.manager.modal_state = self.modal
        self.modal.ids.tags_txt.text = self.ids.tags_label.text 
        self.modal.ids.but1.bind(on_release = self.create_tags)
        self.modal.open()

    #method that changes the text in the tags label
    def create_tags(self,b):
        self.ids.tags_label.text = self.modal.ids.tags_txt.text


    #method that changes the textfor the deck selecter modalview
    def chg_text_md2(self, b):
        self.ids.butd.text = b.text
        self.modal.dismiss()

    #method that changes the text from the cardtype modalview
    def chg_text(self, *args):
        if args[1]:
            self.index = args[1] - 1
            self.ids.butp.text = args[0]
        else:
            self.ids.butd.text = args[0]
