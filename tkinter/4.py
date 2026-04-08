import tkinter as tk
from tkinter import messagebox

def sumar():
    #try: es una estructura de control que permite manejar errores (excepciones) de forma elegante, 
    # evitando que el programa se detenga bruscamente cuando ocurre un error.
    try:
        # Obtener y convertir los valores
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        # Calcular suma
        suma = num1 + num2
        
        # Mostrar resultado en ventana emergente
        messagebox.showinfo("Resultado de la suma", 
                           f"{num1} + {num2} = {suma}")
        
    except ValueError:
        # Error si no son números válidos
        messagebox.showerror("Error", 
                            "¡Por favor ingresa números válidos!")

# Crear ventana
ventana = tk.Tk()
ventana.title("Suma de números")
ventana.geometry("300x200")

# Etiquetas y campos
tk.Label(ventana, text="Número 1:").pack(pady=5)
entry1 = tk.Entry(ventana)
entry1.pack(pady=5)

tk.Label(ventana, text="Número 2:").pack(pady=5)
entry2 = tk.Entry(ventana)
entry2.pack(pady=5)

# Botón para sumar
tk.Button(ventana, text="Sumar", command=sumar, bg="green", fg="white").pack(pady=20)

ventana.mainloop()