from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from amazonScrape import *
from walmartScrape import *
from scrapeAlgo import *

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2
        self.inside.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)
        self.inside.add_widget(Label(text="Price Limit:"))
        self.pricing = TextInput(multiline=False)
        self.inside.add_widget(self.pricing)
        self.inside.add_widget(Label(text="Desired Rating: "))
        self.rating = TextInput(multiline=False)
        self.inside.add_widget(self.rating)

        self.add_widget(self.inside)
        self.submit = Button(text="submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instances):
        scrapeMain(str(self.name.text))
        walmartScrapeMain(str(self.name.text))
        tags = {
            "rating": self.rating.text,
            "pricing": self.pricing.text
        }
        recAlgo(tags)

        

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()


