from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class miles_to_kilometres(App):
    def build(self):
        Window.size = (400, 300)
        self.title = "Converting Calculator"
        self.root = Builder.load_file('converting.kv')
        return self.root

    def handle_calculate(self, value):
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)

    def handle_increment(self,increment):
            self.root.ids.input_number.text = str(int(self.root.ids.input_number.text) + increment)




miles_to_kilometres().run()
