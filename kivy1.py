from kivy.app import App
from kivy.uix.label import Label
class MainApp(App):
    def build(self):
        label = Label(text = 'hello world',
                size_hint =(200, 200),
                pos_hint = {'center_x' : .5,'center_y' : .5})
        return label
if __name__ == '__main__':
    app = MainApp()
    app.run()

