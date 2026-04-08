import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime

class RegistroPersonas:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Personas")
        self.root.geometry("500x550")
        self.root.resizable(False, False)
        
        # Archivo donde se guardarán los datos
        self.archivo_datos = "personas.json"
        
        # Crear archivo JSON si no existe
        self.crear_archivo_json()
        
        # Configurar estilo
        self.root.configure(bg='#f0f0f0')
        
        # Título
        titulo = tk.Label(root, text="Registro de Personas", 
                          font=("Arial", 20, "bold"), 
                          bg='#f0f0f0', fg='#333')
        titulo.pack(pady=20)
        
        # Frame principal para los campos
        frame_form = tk.Frame(root, bg='#f0f0f0')
        frame_form.pack(pady=10, padx=20, fill='both')
        
        # Campos del formulario
        self.campos = {}
        campos_labels = {
            'nombre': 'Nombre completo: *',
            'edad': 'Edad:',
            'email': 'Correo electrónico:',
            'telefono': 'Teléfono:',
            'direccion': 'Dirección:',
            'ocupacion': 'Ocupación:'
        }
        
        for i, (campo, label) in enumerate(campos_labels.items()):
            # Label
            lbl = tk.Label(frame_form, text=label, 
                          font=("Arial", 10),
                          bg='#f0f0f0', fg='#555')
            lbl.grid(row=i, column=0, sticky='w', pady=5, padx=5)
            
            # Entry o Text para dirección
            if campo == 'direccion':
                entry = tk.Text(frame_form, height=3, width=35, 
                               font=("Arial", 10))
                entry.grid(row=i, column=1, pady=5, padx=5)
            else:
                entry = tk.Entry(frame_form, font=("Arial", 10), width=35)
                entry.grid(row=i, column=1, pady=5, padx=5)
            
            self.campos[campo] = entry
        
        # Frame para el botón
        frame_boton = tk.Frame(root, bg='#f0f0f0')
        frame_boton.pack(pady=20)
        
        # Botón Guardar
        btn_guardar = tk.Button(frame_boton, text="Guardar Registro", 
                               command=self.guardar_registro,
                               bg='#4CAF50', fg='white', 
                               font=("Arial", 11, "bold"),
                               padx=40, pady=10, cursor="hand2")
        btn_guardar.pack()
        
        # Texto informativo
        info = tk.Label(root, text="* Campo obligatorio", 
                       font=("Arial", 8), bg='#f0f0f0', fg='#888')
        info.pack(pady=5)
    
    def crear_archivo_json(self):
        """Crea el archivo JSON si no existe"""
        if not os.path.exists(self.archivo_datos):
            with open(self.archivo_datos, 'w', encoding='utf-8') as file:
                json.dump([], file, ensure_ascii=False, indent=4)
    
    def guardar_registro(self):
        """Guarda los datos de la persona en el archivo JSON"""
        # Validar campos obligatorios
        nombre = self.campos['nombre'].get().strip()
        if not nombre:
            messagebox.showwarning("Advertencia", "El nombre es obligatorio")
            self.campos['nombre'].focus()
            return
        
        # Recopilar datos
        persona = {
            'id': self.generar_id(),
            'fecha_registro': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'nombre': nombre,
            'edad': self.campos['edad'].get().strip(),
            'email': self.campos['email'].get().strip(),
            'telefono': self.campos['telefono'].get().strip(),
            'direccion': self.campos['direccion'].get("1.0", tk.END).strip(),
            'ocupacion': self.campos['ocupacion'].get().strip()
        }
        
        try:
            # Leer datos existentes
            with open(self.archivo_datos, 'r', encoding='utf-8') as file:
                personas = json.load(file)
            
            # Agregar nueva persona
            personas.append(persona)
            
            # Guardar en archivo
            with open(self.archivo_datos, 'w', encoding='utf-8') as file:
                json.dump(personas, file, ensure_ascii=False, indent=4)
            
            messagebox.showinfo("Éxito", f"¡Registro guardado exitosamente!\nID: {persona['id']}")
            self.limpiar_formulario()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar: {str(e)}")
    
    def generar_id(self):
        """Genera un ID único para cada registro"""
        try:
            with open(self.archivo_datos, 'r', encoding='utf-8') as file:
                personas = json.load(file)
            return len(personas) + 1
        except:
            return 1
    
    def limpiar_formulario(self):
        """Limpia todos los campos del formulario"""
        for campo, entry in self.campos.items():
            if campo == 'direccion':
                entry.delete("1.0", tk.END)
            else:
                entry.delete(0, tk.END)
        
        # Poner foco en el campo nombre
        self.campos['nombre'].focus()

# Ejecutar programa
if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroPersonas(root)
    root.mainloop()