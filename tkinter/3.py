import tkinter as tk

ventana = tk.Tk()
ventana.title("Formulario con grid")
ventana.geometry("300x250")

# Crear widgets
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
nombre_entry = tk.Entry(ventana)
nombre_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Email:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
email_entry = tk.Entry(ventana)
email_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(ventana, text="Edad:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
edad_entry = tk.Entry(ventana)
edad_entry.grid(row=2, column=1, padx=5, pady=5)

def guardar():
    print(f"Nombre: {nombre_entry.get()}")
    print(f"Email: {email_entry.get()}")
    print(f"Edad: {edad_entry.get()}")

tk.Button(ventana, text="Guardar", command=guardar, bg="blue", fg="white").grid(row=3, column=0, columnspan=2, pady=20)

ventana.mainloop()