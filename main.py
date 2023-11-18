from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
#to set the app size import the bellow module
from kivy.core.window import Window
#from kivy.accordion import Accordion

#set the app size:
#Window.size = (600 , 400)



Builder.load_file('checkbox.kv')

class MyLayout (Widget):
    def checkbox_click (self , instance , value):
        if value :
            self.ids.output.text = "True"
        else :
            self.ids.output.text = "False"

class CalculatorApp (App):
    def build (self):
        Window.clearcolor = (0,0,0,1)
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()