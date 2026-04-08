#Reloj digital
import tkinter as tk
import time

def actualizar_reloj():
    hora_actual = time.strftime("%H:%M:%S")
    fecha_actual = time.strftime("%d/%m/%Y")
    reloj.config(text=hora_actual)
    fecha.config(text=fecha_actual)
    ventana.after(1000, actualizar_reloj)  # Actualizar cada segundo

ventana = tk.Tk()
ventana.title("Reloj Digital")
ventana.geometry("300x150")
ventana.configure(bg="black")

# Estilo
fuente_reloj = ("Arial", 48, "bold")
fuente_fecha = ("Arial", 14)

reloj = tk.Label(ventana, font=fuente_reloj, bg="black", fg="lime")
reloj.pack(expand=True)

fecha = tk.Label(ventana, font=fuente_fecha, bg="black", fg="white")
fecha.pack()

actualizar_reloj()
ventana.mainloop()