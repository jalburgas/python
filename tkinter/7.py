#Menús desplegables
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk, messagebox  # Importar ttk explícitamente

def mostrar_seleccion():
    seleccion = combo.get()
    messagebox.showinfo("Selección", f"Elegiste: {seleccion}")

ventana = tk.Tk()
ventana.title("Menú desplegable")
ventana.geometry("300x200")

# Crear menú desplegable
opciones = ["Python", "Java", "JavaScript", "C++", "HTML/CSS"]
combo = tk.ttk.Combobox(ventana, values=opciones, state="readonly")
combo.set("Elige un lenguaje")
combo.pack(pady=20)

boton = tk.Button(ventana, text="Mostrar", command=mostrar_seleccion)
boton.pack()

ventana.mainloop()