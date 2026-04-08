#Canvas (dibujo básico)
import tkinter as tk

ventana = tk.Tk()
ventana.title("Canvas - Dibujo básico")
ventana.geometry("400x400")

# Crear canvas
canvas = tk.Canvas(ventana, width=400, height=400, bg="white")
canvas.pack()

# Dibujar formas
canvas.create_rectangle(50, 50, 150, 150, fill="blue", outline="black")
canvas.create_oval(200, 50, 300, 150, fill="red", outline="black")
canvas.create_line(50, 200, 350, 200, fill="green", width=3)
canvas.create_text(200, 300, text="¡Hola Canvas!", font=("Arial", 20))

ventana.mainloop()