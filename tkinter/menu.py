import tkinter as tk

def opcion_seleccionada(opcion):
    print(f"Seleccionaste: {opcion}")

ventana = tk.Tk()
ventana.title("Menubutton Ejemplo")
ventana.geometry("300x200")

# Crear Menubutton
menu_btn = tk.Menubutton(ventana, text="📋 Selecciona una opción", 
                          bg="lightblue", font=("Arial", 12))
menu_btn.pack(pady=50)

# Crear el menú que se desplegará
menu = tk.Menu(menu_btn, tearoff=0)  # tearoff=0 quita la línea punteada
menu_btn.config(menu=menu)

# Agregar opciones al menú
menu.add_command(label="✅ Opción 1", command=lambda: opcion_seleccionada("Opción 1"))
menu.add_command(label="✅ Opción 2", command=lambda: opcion_seleccionada("Opción 2"))
menu.add_command(label="✅ Opción 3", command=lambda: opcion_seleccionada("Opción 3"))

# Separador
menu.add_separator()

# Submenú
submenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="📁 Submenú", menu=submenu)
submenu.add_command(label="Sub Opción A", command=lambda: opcion_seleccionada("Sub A"))
submenu.add_command(label="Sub Opción B", command=lambda: opcion_seleccionada("Sub B"))

ventana.mainloop()
