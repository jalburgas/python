import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import re

# Configurar tamaño de ventana para pruebas (opcional)
Window.size = (400, 600)

class LoginForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [30, 50]
        self.spacing = 20
        
        # Título
        self.title_label = Label(
            text="Iniciar Sesión",
            font_size='28sp',
            size_hint_y=0.2,
            color=get_color_from_hex('#2c3e50'),
            bold=True
        )
        self.add_widget(self.title_label)
        
        # Formulario
        form_layout = GridLayout(cols=1, spacing=15, size_hint_y=None)
        form_layout.bind(minimum_height=form_layout.setter('height'))
        
        # Campo de email
        self.email_input = TextInput(
            hint_text='Correo electrónico',
            multiline=False,
            size_hint_y=None,
            height=50,
            padding=[15, 10, 15, 10],
            font_size='16sp'
        )
        form_layout.add_widget(self.email_input)
        
        # Campo de contraseña
        self.password_input = TextInput(
            hint_text='Contraseña',
            multiline=False,
            password=True,
            size_hint_y=None,
            height=50,
            padding=[15, 10, 15, 10],
            font_size='16sp'
        )
        form_layout.add_widget(self.password_input)
        
        # Botón de login
        self.login_button = Button(
            text='INGRESAR',
            size_hint_y=None,
            height=50,
            font_size='16sp',
            background_normal='',
            background_color=get_color_from_hex('#3498db'),
            color=(1, 1, 1, 1)
        )
        self.login_button.bind(on_press=self.validate_login)
        form_layout.add_widget(self.login_button)
        
        self.add_widget(form_layout)
        
    def validate_login(self, instance):
        """Validar credenciales"""
        email = self.email_input.text.strip()
        password = self.password_input.text.strip()
        
        # Validación básica
        if not email or not password:
            self.show_message('Error', 'Por favor completa todos los campos')
            return
            
        if not self.validate_email(email):
            self.show_message('Error', 'Correo electrónico inválido')
            return
        
        # Validación de ejemplo
        if email == 'admin@ejemplo.com' and password == '1234':
            self.show_message('Éxito', '¡Bienvenido!')
            # Aquí puedes cambiar a la pantalla principal
        else:
            self.show_message('Error', 'Usuario o contraseña incorrectos')
    
    def validate_email(self, email):
        """Validar formato de email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def show_message(self, title, message):
        """Mostrar mensaje"""
        content = BoxLayout(orientation='vertical', padding=20, spacing=10)
        content.add_widget(Label(text=message, font_size='14sp'))
        
        close_button = Button(text='Aceptar', size_hint_y=None, height=40)
        content.add_widget(close_button)
        
        popup = Popup(
            title=title,
            content=content,
            size_hint=(0.8, 0.4),
            title_size='18sp'
        )
        
        close_button.bind(on_press=popup.dismiss)
        popup.open()

class LoginApp(App):
    def build(self):
        self.title = 'Login Simple'
        return LoginForm()
    
    def on_start(self):
        from kivy.core.window import Window
        Window.clearcolor = get_color_from_hex('#ecf0f1')

if __name__ == '__main__':
    LoginApp().run()