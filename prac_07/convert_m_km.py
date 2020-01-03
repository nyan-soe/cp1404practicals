"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
Nyan Soe
Started 3/1/2020
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

__author__ = 'Nyan Soe'


class ConvertMilesToKilometersApp(App):
    """ ConvertMilesToKilometersApp is a Kivy App for converting miles to kilometres """

    answer = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) * 1.6093
            self.answer = str(result)
        except ValueError:
            self.answer = "Please input number"

    def handle_increment(self, value):
        """ handle increment and decrement when up/down button is pressed"""
        try:
            if float(self.root.ids.input_number.text) + value < 0:
                self.root.ids.input_number.text = "0"
            else:
                self.root.ids.input_number.text = str(float(self.root.ids.input_number.text) + value)
        except ValueError:
            self.answer = "Please input number"


ConvertMilesToKilometersApp().run()
