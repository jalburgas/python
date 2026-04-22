import tkinter as tk
from tkinter import messagebox

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Simple")
ventana.geometry("400x500")
ventana.configure(bg="#f0f0f0")

# Variables
num1 = tk.StringVar()
num2 = tk.StringVar()
resultado = tk.StringVar()

# Funciones de cálculo
def sumar():
    try:
        r = float(num1.get()) + float(num2.get())
        resultado.set(f"Resultado: {r}")
    except:
        messagebox.showerror("Error", "Ingrese números válidos")

def restar():
    try:
        r = float(num1.get()) - float(num2.get())
        resultado.set(f"Resultado: {r}")
    except:
        messagebox.showerror("Error", "Ingrese números válidos")

def multiplicar():
    try:
        r = float(num1.get()) * float(num2.get())
        resultado.set(f"Resultado: {r}")
    except:
        messagebox.showerror("Error", "Ingrese números válidos")

def dividir():
    try:
        if float(num2.get()) == 0:
            messagebox.showerror("Error", "No se puede dividir entre cero")
        else:
            r = float(num1.get()) / float(num2.get())
            resultado.set(f"Resultado: {r}")
    except:
        messagebox.showerror("Error", "Ingrese números válidos")

def limpiar():
    num1.set("")
    num2.set("")
    resultado.set("Resultado: ")
    entry1.focus()

# Interfaz gráfica
titulo = tk.Label(ventana, text="CALCULADORA BÁSICA", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
titulo.pack(pady=20)

# Número 1
tk.Label(ventana, text="Número 1:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
entry1 = tk.Entry(ventana, textvariable=num1, font=("Arial", 14), width=15, justify="center")
entry1.pack(pady=5)

# Número 2
tk.Label(ventana, text="Número 2:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
entry2 = tk.Entry(ventana, textvariable=num2, font=("Arial", 14), width=15, justify="center")
entry2.pack(pady=5)

# Botones
frame_botones = tk.Frame(ventana, bg="#f0f0f0")
frame_botones.pack(pady=20)

tk.Button(frame_botones, text="➕ SUMAR", command=sumar, width=10, bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_botones, text="➖ RESTAR", command=restar, width=10, bg="#2196F3", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_botones, text="✖️ MULTIPLICAR", command=multiplicar, width=10, bg="#FF9800", fg="white", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_botones, text="➗ DIVIDIR", command=dividir, width=10, bg="#f44336", fg="white", font=("Arial", 10, "bold")).grid(row=1, column=1, padx=5, pady=5)

# Botón limpiar
tk.Button(ventana, text="🗑️ LIMPIAR", command=limpiar, width=20, bg="#9E9E9E", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

# Resultado
tk.Label(ventana, text="RESULTADO:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=10)
resultado_label = tk.Label(ventana, textvariable=resultado, font=("Arial", 16, "bold"), bg="#ffffff", fg="#333", width=25, height=2, relief="sunken")
resultado_label.pack(pady=10)

# Iniciar programa
entry1.focus()
ventana.mainloop()
