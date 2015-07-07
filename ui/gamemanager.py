from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.dropdown import DropDown
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.properties import (ObjectProperty, NumericProperty, OptionProperty, DictProperty,
                             BooleanProperty, StringProperty, ListProperty)
from storage.simple_implementation import SimpleImplementation
from storage.database_manager import DatabaseManager


class GameManager(ScreenManager):

    # variable that helps us keep track of the current deck
    current_deck = ObjectProperty(None)
    # variable that helps us know if we currently have a modalview dispalyed
    modal_state = ObjectProperty(1)

    ## mainbutton nu are rost aici , trebuie implementat altfel !

    mainbutton = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(GameManager, self).__init__(**kwargs)
        # creating our storage manager
        self.manager = DatabaseManager(SimpleImplementation())


        #creating an all cards deck (not necesary if we can disaply the all cards some other way)
        name = self.manager.create_attribute("name","string","All Cards")
        deck = self.manager.create_deck([],[name, ])
        self.manager.add_deck(deck)
        # generate some default data
        self.manager.generate_data()
        for decks in self.manager.implementation.decks:
            for card in decks.cards_:
                self.manager.implementation.decks[0].cards_.append(card)
        #self.current="add_card"

    # method called from PlayDeck to switch to Study
    def switch_to_study(self, *args):
        self.current_deck = self.manager.find_deck_by_attribute("name",self.ids.s6.ids.deck_label.text)[0]
        #reseting the counter for cards played in study
        self.ids.s7.i = 0
        # changing the actionlabel text from study to display the currently played deck
        self.ids.s7.ids.stal.text = 'Study ' + self.current_deck.find_attribute("name").attribute_value_
        #reset the Study screen before switching to it
        self.ids.s7.reset()
        self.current = 'study'

    #method called from SoloMenu to switch to PlayDeck
    def switch_to_deckplay(self , button ):
        #changing the deck_label text and the actionlabel text to the text of the button we just released from the decks button in SoloMenu
        self.ids.s6.ids.deck_label.text = button.text
        self.ids.s6.ids.action_deck_label.text = button.text
        self.current = 'play_deck'

    #method called from PlayDeck to switch to AddCard
    def set_deck(self,text):
        #changing the text of the deck selecter button into the name of our current deck
        self.ids.s3.ids.butd.text = text
        self.current = 'add_card'

    #method called from CardBrowser to switch to AddCard
    def switch_to_add_card(self, *args):
        #selecting the card we just pressed from the cardbrowser
        self.current_screen.current_card = self.manager.find_card_by_qa(self.manager.find_question_by_attribute("question",args[0].text)[0])
        #changing the create card button into save changes button
        self.ids.s3.ids.ac_create_card.text = 'Save changes'
        #making sure we display our cards question and answer in AddCard
        self.ids.s3.ids.lab_q.text = args[0].text
        self.ids.s3.ids.lab_a.text = self.manager.find_card_by_qa(self.manager.find_question_by_attribute("question",args[0].text)[0]).answers_[0].find_attribute("answer").attribute_value_
        self.current = 'add_card'

    #method called from the sidepanel to switch to CardBrowser
    def switch_to_card_browser(self):
        self.current = 'card_browser'

        #creating a dropdown for the user to select deck
        dropdown = DropDown()
        self.ids.s8.ids.ddbox.clear_widgets()

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
                         background_normal = '')
            btn.fast_bind('on_release', self.dd_select,btn,dropdown)
            dropdown.add_widget(btn)

        dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))

        #dispalying the cards
        self.cb_display_cards('basic',self.mainbutton)

    def dd_select(self, *args):
        args[1].select(args[0].text)
        self.cb_display_cards('basic',args[0])

    #method to display the cards
    def cb_display_cards(self, *args):

 ## TODO:
        """ Add search bar in the ActionBar by inheriting it from ActionItem """


 ## BUG:
        """ Find a way to cancel re.search() special regex characters . We want it to look
            only normal """

 ## TODO:
        """ Add better implementation of this """

        #clear all previous dispalys
        self.ids.s8.ids.gl.clear_widgets()
        self.ids.s8.ids.search.state = 'normal'
        # checking if we want to display after a search or after a selected deck( 'basic' is for decks and 'search' is for search)
        if args[0] is 'basic':
            # dispaying the cards of the deck indicated by the dropdown's mainbutton
            for card in self.manager.find_deck_by_attribute("name",args[1].text)[0].cards_:#find_deck_by_attribute("name",args[1].text)[0].cards_:
                self.ids.s8.ids.gl.add_widget(Button(size_hint_y = None,
                                                     height = '25dp',
                                                     text = card.question_.find_attribute("question").attribute_value_ ,#.replace(args[2],'[color=#FF0000]%s[/color]' % args[2]) ,
                                                     color = [0,0,0,1] ,
                                                     background_color = [1,1,1,1] ,
                                                     background_normal = '' ,
                                                     background_down = '',
                                                     on_release = self.switch_to_add_card))

                self.ids.s8.ids.gl.add_widget(Button(size_hint_y = None,
                                                     height = '25dp',
                                                     text = card.answers_[0].find_attribute("answer").attribute_value_ ,#.replace(args[2],'[color=#FF0000]%s[/color]' % args[2]) ,
                                                     color = [0,0,0,1] ,
                                                     background_color = [1,1,1,1] ,
                                                     background_normal = '' ,
                                                     background_down = '',
                                                     on_release = self.switch_to_add_card))
        elif args[0] is 'search':
            #displaying only the cards of the deck indicated by the dropdown's mainbuuton
            for card in self.manager.find_deck_by_attribute("name",args[1].text)[0].cards_:#find_deck_by_attribute("name",args[1].text)[0].cards_:
                #looking for our searchinput in questions or answers
                if args[2] in card.question_.find_attribute("question").attribute_value_ or \
                    args[2] in card.answers_[0].find_attribute("answer").attribute_value_:
                    self.ids.s8.ids.gl.add_widget(Button(size_hint_y = None,
                                                         markup = True ,
                                                         height = '25dp',
                                                         color = [0,0,0,1] ,
                                                         text = card.question_.find_attribute("question").attribute_value_ ,#.replace(args[2],'[color=#FF0000]%s[/color]' % args[2]) ,
                                                         background_color = [1,1,1,1] ,
                                                         background_normal = '' ,
                                                         background_down = '',
                                                         on_release = self.switch_to_add_card))

                    self.ids.s8.ids.gl.add_widget(Button(size_hint_y = None,
                                                         markup = True ,
                                                         height = '25dp',
                                                         color = [0,0,0,1] ,
                                                         text = card.answers_[0].find_attribute("answer").attribute_value_ ,#.replace(args[2],'[color=#FF0000]%s[/color]' % args[2]) ,
                                                         background_color = [1,1,1,1] ,
                                                         background_normal = '' ,
                                                         background_down = '',
                                                         on_release = self.switch_to_add_card))


    #method to switch to SoloMenu
    def switch_to_solo_menu(self):
        self.current = 'main_menu'
        #recreating our gridlayout
        for deck in self.manager.implementation.decks:
            btn = Button(color = (0,0,0,1),
                        text = deck.find_attribute("name").attribute_value_,
                        size_hint_y = None,
                        height = '50dp',
                        background_normal = '',
                        background_color = (1,1,1,1),
                        on_release = self.switch_to_deckplay)
            self.ids.s5.ids.gl1.add_widget(btn)
