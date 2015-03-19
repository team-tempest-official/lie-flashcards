from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.uix.stencilview import StencilView
from kivy.uix.scrollview import ScrollView
from kivy.effects.scroll import ScrollEffect
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.properties import ObjectProperty



class CustomModal2(ModalView):

    mn = ObjectProperty(None)
    scrn = ObjectProperty(None)

    def __init__(self, man, screen, **kwargs):
        super(CustomModal2, self).__init__(**kwargs)
        #saving the storage manager and the AddCard screen
        self.mn = man
        self.scrn = screen

        # displaying all the decks by creating a button for each deck we find exept the 'all cards' deck(decks[0])
        for d in self.mn.implementation.decks:
            if d is not self.mn.implementation.decks[0]:
                b = Button(text = d.find_attribute("name").attribute_value_ ,
                            background_normal = '' ,
                            color = [0,0,0,1] ,
                            background_color = [1,1,1,1] ,
                            on_release = self.scrn.chg_text_md2 )
                #we have to increase the height of our gridlayout 
                self.ids.gl1.height += b.height / 2
                # if the modalview's height reaches 300 we stop increasing it(we still have scrollview)
                if self.height < '300dp':
                    self.height += b.height / 2
                self.ids.gl1.add_widget(b)
                print self.height
