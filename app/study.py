from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionBar , ActionItem, ActionButton
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.properties import  NumericProperty

from storage.simple_implementation import SimpleImplementation
from storage.database_manager import DatabaseManager



class Study(Screen):

    i = NumericProperty(1)

    def __init__(self, **kwargs):
        super(Study, self).__init__(**kwargs)

    #method to reset screen when done with a card
    def reset(self, *args):
        #destroy what we previously had in the buttonslayout
        self.ids.bl_ans.clear_widgets()
        #recreate the 'show answer button'
        self.ids.bl_ans.add_widget(Button(text = "Show Answer",
                                            color = [0,0,0,1] ,
                                            background_normal =  '' ,
                                            background_color= [1,1,1,1] ,
                                            on_release = self.show_ans))
        #display the new question through self.i counter and set the answer to ''
        self.ids.lab1.text = self.manager.current_deck.cards_[self.i].question_.find_attribute("question").attribute_value_
        self.ids.lab2.text = ''
        #increase counter
        self.i += 1

    #method to show answer
    def show_ans(self, *args):
        #destroy what we previously had in the buttonslayout
        self.ids.bl_ans.clear_widgets()
        #show answer
        self.ids.lab2.text = self.manager.current_deck.cards_[self.i - 1].answers_[0].find_attribute("answer").attribute_value_
        #recreate the 3 buttons 
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
