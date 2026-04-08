from kivy.app import App
from kivy.uix.label import Label

class HolaApp(App):
    def build(self):
        # Crea una etiqueta que diga "¡Hola, Kivy!"
        return Label(text='¡Hola, Kivy!', font_size=40)

if __name__ == '__main__':
    HolaApp().run()