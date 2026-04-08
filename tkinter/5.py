#Validación de entrada numérica
import tkinter as tk
from tkinter import messagebox

def procesar_numero():
    try:
        # Intentar convertir a número
        numero = float(entrada.get())
        
        # Si llegamos aquí, la conversión fue exitosa
        messagebox.showinfo("Éxito", f"El número es: {numero}")
        
    except ValueError:
        # Se ejecuta si no se pudo convertir a número
        messagebox.showerror("Error", "¡No ingresaste un número válido!")

ventana = tk.Tk()
ventana.title("Validación con try")
ventana.geometry("300x150")

tk.Label(ventana, text="Ingresa un número:").pack(pady=10)
entrada = tk.Entry(ventana)
entrada.pack(pady=5)
tk.Button(ventana, text="Procesar", command=procesar_numero).pack(pady=10)

ventana.mainloop()