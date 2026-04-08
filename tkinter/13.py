import tkinter as tk
from tkinter import colorchooser

def elegir_color():
    color = colorchooser.askcolor(title="Elige un color")
    if color[1]:  # color[1] es el código hexadecimal
        ventana.config(bg=color[1])
        etiqueta.config(text=f"Color seleccionado: {color[1]}")

ventana = tk.Tk()
ventana.title("Selector de color")
ventana.geometry("300x200")

boton = tk.Button(ventana, text="Elegir color de fondo", command=elegir_color)
boton.pack(pady=20)

etiqueta = tk.Label(ventana, text="Color no seleccionado")
etiqueta.pack()
#La función pack() en Tkinter (Python) es un geometry manager que organiza los widgets 
# en bloques antes de colocarlos en la ventana principal.

ventana.mainloop()