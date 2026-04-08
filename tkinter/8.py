#Barra de progreso
import tkinter as tk
from tkinter import ttk
import time

def iniciar_progreso():
    barra["maximum"] = 100
    for i in range(101):
        barra["value"] = i
        ventana.update()
        time.sleep(0.02)
    etiqueta.config(text="¡Completado!")

ventana = tk.Tk()
ventana.title("Barra de progreso")
ventana.geometry("300x150")

barra = ttk.Progressbar(ventana, length=250, mode='determinate')
barra.pack(pady=20)

boton = tk.Button(ventana, text="Iniciar", command=iniciar_progreso)
boton.pack()

etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

ventana.mainloop()