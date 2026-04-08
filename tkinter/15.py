#Aplicación con pestañas (Notebook)
   # ttk.Notebook es el widget que crea las pestañas
   #fill=tk.BOTH hace que ocupe todo el espacio disponible
   #expand=True permite que se expanda con la ventana

import tkinter as tk
from tkinter import ttk

def crear_pestaña_calculadora(parent):
    frame = ttk.Frame(parent)
    
    num1 = tk.Entry(frame)
    num1.pack(pady=5)
    
    num2 = tk.Entry(frame)
    num2.pack(pady=5)
    
    resultado = tk.Label(frame, text="Resultado: ")
    resultado.pack(pady=5)
    
    def sumar():
        try:
            r = float(num1.get()) + float(num2.get())
            resultado.config(text=f"Resultado: {r}")
        except:
            resultado.config(text="Error: Ingresa números")
    
    btn = tk.Button(frame, text="Sumar", command=sumar)
    btn.pack(pady=5)
    
    return frame

def crear_pestaña_texto(parent):
    frame = ttk.Frame(parent)
    
    texto = tk.Text(frame, height=10, width=30)
    texto.pack(padx=10, pady=10)
    
    def limpiar():
        texto.delete(1.0, tk.END)
    
    btn = tk.Button(frame, text="Limpiar", command=limpiar)
    btn.pack()
    
    return frame

def crear_pestaña_colores(parent):
    frame = ttk.Frame(parent)
    
    colores = ["red", "green", "blue", "yellow", "purple", "orange"]
    
    def cambiar_color(color):
        frame.config(style=f"{color}.TFrame")
        # Crear estilo personalizado
        style = ttk.Style()
        style.configure(f"{color}.TFrame", background=color)
    
    for color in colores:
        btn = tk.Button(frame, text=color, bg=color, 
                       command=lambda c=color: cambiar_color(c))
        btn.pack(pady=2, fill=tk.X, padx=20)
    
    return frame

# Ventana principal
ventana = tk.Tk()
ventana.title("Aplicación con pestañas")
ventana.geometry("400x400")

# Crear el widget de pestañas
notebook = ttk.Notebook(ventana)
notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Crear y agregar pestañas
pestaña1 = crear_pestaña_calculadora(notebook)
pestaña2 = crear_pestaña_texto(notebook)
pestaña3 = crear_pestaña_colores(notebook)

notebook.add(pestaña1, text="Calculadora")
notebook.add(pestaña2, text="Editor")
notebook.add(pestaña3, text="Colores")

ventana.mainloop()

#Esta aplicación demuestra:
#    Organización modular con funciones separadas por pestaña
#    Manejo de diferentes widgets (Entry, Text, Button, Label)
#    Validación de entrada de usuario
#    Personalización dinámica de estilos
#    Estructura de eventos en Tkinter
#Es un excelente ejemplo de cómo crear aplicaciones organizadas y funcionales con interfaces de pestañas en Python.