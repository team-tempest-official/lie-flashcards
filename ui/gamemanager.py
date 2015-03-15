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

    current_deck = ObjectProperty(None)
    modal_state = ObjectProperty(1)

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



    def switch_to_solo_menu(self):
        self.current = 'solo_menu'
        for deck in self.manager.implementation.decks:
            btn = Button(color = (0,0,0,1),
                        text = deck.find_attribute("name").attribute_value_,
                        size_hint_y = None,
                        height = '50dp',
                        background_normal = '',
                        background_color = (1,1,1,1),
                        on_release = self.switch_to_deckplay)
            self.ids.s1.ids.gl1.add_widget(btn)
