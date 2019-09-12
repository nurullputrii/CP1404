from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

MILES_KM = 1.60934

class Mil_Km_Converter(App):
    message = StringProperty()

    def build(self):
        self.title = "Miles to Km converter"
        self.root = Builder.load_file('mil_km_converter.kv')
        return self.root

    def handle_calculate(self):
        value = self.get_validated_miles()
        result = value * MILES_KM
        self.root.ids.output_result.text = str(result)


    def handle_text_input(self):
        self.message = self.root.ids.input_number.text


    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_number.text = str(value)
        self.handle_calculate()



    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0



# create and start the App running
Mil_Km_Converter().run()
