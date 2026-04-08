import tkinter as tk
from tkinter import messagebox
import json
import os

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Archivo para almacenar usuarios
        self.users_file = "users.json"
        
        # Crear archivo de usuarios si no existe
        if not os.path.exists(self.users_file):
            self.create_default_users()
        
        # Variable para controlar el frame actual
        self.current_frame = None
        
        # Mostrar frame de login inicial
        self.show_login_frame()
    
    def create_default_users(self):
        """Crea usuarios por defecto"""
        users = {
            "admin": {"password": "admin123", "email": "admin@ejemplo.com"},
            "usuario1": {"password": "pass123", "email": "user1@ejemplo.com"}
        }
        with open(self.users_file, 'w') as f:
            json.dump(users, f)
    
    def load_users(self):
        """Carga los usuarios del archivo"""
        try:
            with open(self.users_file, 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def save_users(self, users):
        """Guarda los usuarios en el archivo"""
        with open(self.users_file, 'w') as f:
            json.dump(users, f)
    
    def clear_frame(self):
        """Limpia el frame actual"""
        if self.current_frame:
            self.current_frame.destroy()
    
    def show_login_frame(self):
        """Muestra el frame de login"""
        self.clear_frame()
        
        self.current_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.current_frame.pack(fill="both", expand=True)
        
        # Título
        title = tk.Label(self.current_frame, text="Iniciar Sesión", 
                        font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=30)
        
        # Frame para el formulario
        form_frame = tk.Frame(self.current_frame, bg="#f0f0f0")
        form_frame.pack(pady=20)
        
        # Usuario
        tk.Label(form_frame, text="Usuario:", font=("Arial", 12), 
                bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=10)
        self.username_entry = tk.Entry(form_frame, font=("Arial", 12), 
                                      width=25, relief="solid", bd=1)
        self.username_entry.grid(row=0, column=1, pady=10, padx=10)
        
        # Contraseña
        tk.Label(form_frame, text="Contraseña:", font=("Arial", 12), 
                bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=10)
        self.password_entry = tk.Entry(form_frame, font=("Arial", 12), 
                                      width=25, relief="solid", bd=1, show="•")
        self.password_entry.grid(row=1, column=1, pady=10, padx=10)
        
        # Botones
        button_frame = tk.Frame(self.current_frame, bg="#f0f0f0")
        button_frame.pack(pady=20)
        
        login_btn = tk.Button(button_frame, text="Ingresar", 
                             command=self.login, bg="#4CAF50", fg="white",
                             font=("Arial", 12), width=15, height=1)
        login_btn.grid(row=0, column=0, padx=10)
        
        register_btn = tk.Button(button_frame, text="Registrarse", 
                                command=self.show_register_frame, 
                                bg="#2196F3", fg="white",
                                font=("Arial", 12), width=15, height=1)
        register_btn.grid(row=0, column=1, padx=10)
        
        # Vincular tecla Enter para login
        self.root.bind('<Return>', lambda event: self.login())
    
    def show_register_frame(self):
        """Muestra el frame de registro"""
        self.clear_frame()
        
        self.current_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.current_frame.pack(fill="both", expand=True)
        
        # Título
        title = tk.Label(self.current_frame, text="Registro de Usuario", 
                        font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=30)
        
        # Frame para el formulario
        form_frame = tk.Frame(self.current_frame, bg="#f0f0f0")
        form_frame.pack(pady=20)
        
        # Usuario
        tk.Label(form_frame, text="Usuario:", font=("Arial", 12), 
                bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=10)
        self.reg_username_entry = tk.Entry(form_frame, font=("Arial", 12), 
                                          width=25, relief="solid", bd=1)
        self.reg_username_entry.grid(row=0, column=1, pady=10, padx=10)
        
        # Email
        tk.Label(form_frame, text="Email:", font=("Arial", 12), 
                bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=10)
        self.reg_email_entry = tk.Entry(form_frame, font=("Arial", 12), 
                                       width=25, relief="solid", bd=1)
        self.reg_email_entry.grid(row=1, column=1, pady=10, padx=10)
        
        # Contraseña
        tk.Label(form_frame, text="Contraseña:", font=("Arial", 12), 
                bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=10)
        self.reg_password_entry = tk.Entry(form_frame, font=("Arial", 12), 
                                          width=25, relief="solid", bd=1, show="•")
        self.reg_password_entry.grid(row=2, column=1, pady=10, padx=10)
        
        # Confirmar contraseña
        tk.Label(form_frame, text="Confirmar:", font=("Arial", 12), 
                bg="#f0f0f0").grid(row=3, column=0, sticky="w", pady=10)
        self.reg_confirm_entry = tk.Entry(form_frame, font=("Arial", 12), 
                                         width=25, relief="solid", bd=1, show="•")
        self.reg_confirm_entry.grid(row=3, column=1, pady=10, padx=10)
        
        # Botones
        button_frame = tk.Frame(self.current_frame, bg="#f0f0f0")
        button_frame.pack(pady=20)
        
        register_btn = tk.Button(button_frame, text="Registrar", 
                                command=self.register, bg="#4CAF50", fg="white",
                                font=("Arial", 12), width=15, height=1)
        register_btn.grid(row=0, column=0, padx=10)
        
        back_btn = tk.Button(button_frame, text="Volver", 
                            command=self.show_login_frame, 
                            bg="#f44336", fg="white",
                            font=("Arial", 12), width=15, height=1)
        back_btn.grid(row=0, column=1, padx=10)
    
    def login(self):
        """Verifica las credenciales del usuario"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showwarning("Campos vacíos", 
                                  "Por favor, ingrese usuario y contraseña")
            return
        
        users = self.load_users()
        
        if username in users and users[username]["password"] == password:
            messagebox.showinfo("Éxito", f"¡Bienvenido {username}!")
            self.show_main_frame(username)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
            self.password_entry.delete(0, tk.END)
    
    def register(self):
        """Registra un nuevo usuario"""
        username = self.reg_username_entry.get()
        email = self.reg_email_entry.get()
        password = self.reg_password_entry.get()
        confirm = self.reg_confirm_entry.get()
        
        # Validaciones
        if not username or not email or not password:
            messagebox.showwarning("Campos vacíos", 
                                  "Por favor, complete todos los campos")
            return
        
        if password != confirm:
            messagebox.showwarning("Error", "Las contraseñas no coinciden")
            return
        
        if len(password) < 6:
            messagebox.showwarning("Error", 
                                  "La contraseña debe tener al menos 6 caracteres")
            return
        
        if "@" not in email or "." not in email:
            messagebox.showwarning("Error", "Ingrese un email válido")
            return
        
        users = self.load_users()
        
        if username in users:
            messagebox.showwarning("Error", "El usuario ya existe")
            return
        
        # Registrar nuevo usuario
        users[username] = {
            "password": password,
            "email": email
        }
        
        self.save_users(users)
        
        messagebox.showinfo("Éxito", "Usuario registrado correctamente")
        self.show_login_frame()
    
    def show_main_frame(self, username):
        """Muestra la ventana principal después del login"""
        self.clear_frame()
        
        self.current_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.current_frame.pack(fill="both", expand=True)
        
        # Título de bienvenida
        welcome_label = tk.Label(self.current_frame, 
                                text=f"¡Bienvenido, {username}!", 
                                font=("Arial", 24, "bold"), 
                                bg="#f0f0f0", fg="#333")
        welcome_label.pack(pady=50)
        
        # Mensaje de éxito
        message = tk.Label(self.current_frame, 
                          text="Has iniciado sesión correctamente", 
                          font=("Arial", 14), 
                          bg="#f0f0f0", fg="#666")
        message.pack(pady=20)
        
        # Botón para cerrar sesión
        logout_btn = tk.Button(self.current_frame, text="Cerrar Sesión", 
                              command=self.show_login_frame, 
                              bg="#f44336", fg="white",
                              font=("Arial", 12), width=20, height=2)
        logout_btn.pack(pady=30)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()