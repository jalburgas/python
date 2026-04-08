"""Archivo principal de la aplicación Kivy. (logica de negocio)"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder  # <-- Esta es la importación que falta

Builder.load_file('mi_app.kv')

class MainWidget(BoxLayout):
    # Propiedades para vincular con el archivo kv
    texto_ingresado = StringProperty('')
    texto_salida = StringProperty('')
    
    def procesar_texto(self):
        # Lógica de negocio
        self.texto_salida = f"Procesado: {self.texto_ingresado}"
    
    def limpiar_campos(self):
        self.texto_ingresado = ''
        self.texto_salida = ''

class MiApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    MiApp().run()