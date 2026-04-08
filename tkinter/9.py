import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro?")
    if respuesta:
        messagebox.showinfo("Info", "¡Confirmaste!")
    else:
        messagebox.showwarning("Advertencia", "Cancelaste la operación")

def mostrar_error():
    messagebox.showerror("Error", "Algo salió mal")

ventana = tk.Tk()
ventana.title("Mensajes emergentes")
ventana.geometry("300x200")

btn_confirmar = tk.Button(ventana, text="Mostrar confirmación", command=mostrar_mensaje)
btn_confirmar.pack(pady=10)

btn_error = tk.Button(ventana, text="Mostrar error", command=mostrar_error)
btn_error.pack()

ventana.mainloop()