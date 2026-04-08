import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.utils import get_color_from_hex
import re

# Configurar tamaño de ventana para pruebas (opcional)
Window.size = (400, 600)

class RoundedButton(Button):
    """Botón personalizado con bordes redondeados"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = get_color_from_hex('#3498db')
        self.color = (1, 1, 1, 1)
        self.border_radius = [20]
        
    def on_press(self):
        self.background_color = get_color_from_hex('#2980b9')
        super().on_press()
        
    def on_release(self):
        self.background_color = get_color_from_hex('#3498db')
        super().on_release()

class LoginForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [30, 50]
        self.spacing = 20
        
        # Título de la aplicación
        self.title_label = Label(
            text="Bienvenido",
            font_size='24sp',
            size_hint_y=0.2,
            color=get_color_from_hex('#2c3e50')
        )
        self.add_widget(self.title_label)
        
        # Formulario de login
        form_layout = GridLayout(cols=1, spacing=15, size_hint_y=None)
        form_layout.bind(minimum_height=form_layout.setter('height'))
        
        # Campo de email/usuario
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
        self.login_button = RoundedButton(
            text='INICIAR SESIÓN',
            size_hint_y=None,
            height=50,
            font_size='16sp'
        )
        self.login_button.bind(on_press=self.validate_login)
        form_layout.add_widget(self.login_button)
        
        # Botón de registro (opcional)
        self.register_button = Button(
            text='¿No tienes cuenta? Regístrate',
            size_hint_y=None,
            height=40,
            background_normal='',
            color=get_color_from_hex('#3498db'),
            font_size='14sp'
        )
        self.register_button.bind(on_press=self.show_register_popup)
        form_layout.add_widget(self.register_button)
        
        # ScrollView para el formulario
        scroll = ScrollView(size_hint=(1, 0.6))
        scroll.add_widget(form_layout)
        self.add_widget(scroll)
        
    def validate_login(self, instance):
        """Validar credenciales de login"""
        email = self.email_input.text.strip()
        password = self.password_input.text.strip()
        
        # Validación básica
        if not email or not password:
            self.show_popup('Error', 'Por favor completa todos los campos')
            return
            
        if not self.validate_email(email):
            self.show_popup('Error', 'Correo electrónico inválido')
            return
            
        # Aquí iría la validación con una base de datos o API
        # Por ahora, usamos credenciales de prueba
        if email == 'usuario@ejemplo.com' and password == '123456':
            self.show_popup('Éxito', '¡Login exitoso!')
            # Aquí puedes navegar a la pantalla principal
        else:
            self.show_popup('Error', 'Credenciales incorrectas')
    
    def validate_email(self, email):
        """Validar formato de email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def show_popup(self, title, message):
        """Mostrar popup con mensaje"""
        content = BoxLayout(orientation='vertical', padding=20, spacing=10)
        content.add_widget(Label(text=message, font_size='14sp'))
        
        close_button = Button(text='Cerrar', size_hint_y=None, height=40)
        content.add_widget(close_button)
        
        popup = Popup(
            title=title,
            content=content,
            size_hint=(0.8, 0.4),
            title_size='18sp'
        )
        
        close_button.bind(on_press=popup.dismiss)
        popup.open()
    
    def show_register_popup(self, instance):
        """Mostrar popup de registro"""
        # Crear formulario de registro
        register_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        register_layout.add_widget(Label(text='Registro de Usuario', font_size='18sp', size_hint_y=0.2))
        
        nombre_input = TextInput(hint_text='Nombre completo', multiline=False, size_hint_y=None, height=40)
        register_layout.add_widget(nombre_input)
        
        email_input = TextInput(hint_text='Correo electrónico', multiline=False, size_hint_y=None, height=40)
        register_layout.add_widget(email_input)
        
        password_input = TextInput(hint_text='Contraseña', multiline=False, password=True, size_hint_y=None, height=40)
        register_layout.add_widget(password_input)
        
        confirm_password = TextInput(hint_text='Confirmar contraseña', multiline=False, password=True, size_hint_y=None, height=40)
        register_layout.add_widget(confirm_password)
        
        register_btn = Button(text='Registrarse', size_hint_y=None, height=40)
        register_layout.add_widget(register_btn)
        
        popup = Popup(
            title='Registro',
            content=register_layout,
            size_hint=(0.9, 0.7)
        )
        
        def register_user(instance):
            # Lógica de registro
            if password_input.text == confirm_password.text and password_input.text:
                popup.dismiss()
                self.show_popup('Éxito', 'Registro exitoso. Por favor inicia sesión.')
            else:
                self.show_popup('Error', 'Las contraseñas no coinciden o están vacías')
        
        register_btn.bind(on_press=register_user)
        popup.open()

class LoginApp(App):
    def build(self):
        # Configurar tema
        self.title = 'Mi Aplicación'
        
        # Layout principal
        main_layout = BoxLayout(orientation='vertical')
        
        # Agregar el formulario de login
        login_form = LoginForm()
        main_layout.add_widget(login_form)
        
        return main_layout
    
    def on_start(self):
        # Configurar la ventana (opcional para Android)
        from kivy.core.window import Window
        Window.clearcolor = get_color_from_hex('#ecf0f1')

if __name__ == '__main__':
    LoginApp().run()