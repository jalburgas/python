import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi aplicación")
ventana.geometry("400x500")

# ========== 1. ETIQUETAS (Label) ==========
etiqueta_bienvenida = tk.Label(ventana, text="¡Bienvenido a mi app!", 
                                font=("Arial", 16, "bold"))
etiqueta_bienvenida.pack(pady=10)

etiqueta_nombre = tk.Label(ventana, text="Nombre:")
etiqueta_nombre.pack()

# ========== 2. CAJA DE TEXTO (Entry) ==========
entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack(pady=5)

# ========== 3. CAJA DE TEXTO MULTILÍNEA (Text) ==========
etiqueta_mensaje = tk.Label(ventana, text="Mensaje:")
etiqueta_mensaje.pack(pady=(10,0))

texto_mensaje = tk.Text(ventana, height=5, width=40)
texto_mensaje.pack(pady=5)

# ========== 4. BOTONES (Button) ==========
def mostrar_datos():
    """Función que se ejecuta al hacer clic en el botón"""
    nombre = entrada_nombre.get()
    mensaje = texto_mensaje.get("1.0", tk.END).strip()
    
    if nombre and mensaje:
        resultado_label.config(text=f"Hola {nombre}, tu mensaje es:\n{mensaje}")
    else:
        resultado_label.config(text="Por favor, completa todos los campos")

boton_enviar = tk.Button(ventana, text="Enviar", 
                         command=mostrar_datos,
                         bg="green", fg="white",
                         padx=20, pady=5)
boton_enviar.pack(pady=10)

# ========== 5. VARIABLES DE CONTROL ==========
# Variable para guardar el estado del checkbox
acepta_terminos = tk.BooleanVar()

# ========== 6. CHECKBOX (Checkbutton) ==========
checkbox = tk.Checkbutton(ventana, text="Acepto los términos y condiciones",
                          variable=acepta_terminos)
checkbox.pack()

# ========== 7. RADIOBUTTONS ==========
etiqueta_opcion = tk.Label(ventana, text="Elige una opción:")
etiqueta_opcion.pack(pady=(10,0))

opcion = tk.StringVar(value="opcion1")

radio1 = tk.Radiobutton(ventana, text="Opción 1", 
                        variable=opcion, value="opcion1")
radio2 = tk.Radiobutton(ventana, text="Opción 2", 
                        variable=opcion, value="opcion2")
radio3 = tk.Radiobutton(ventana, text="Opción 3", 
                        variable=opcion, value="opcion3")

radio1.pack()
radio2.pack()
radio3.pack()

# ========== 8. ETIQUETA PARA RESULTADOS ==========
resultado_label = tk.Label(ventana, text="", 
                           wraplength=350,  # Ajuste de línea
                           fg="blue")
resultado_label.pack(pady=20)

# ========== 9. BOTÓN DE SALIDA ==========
boton_salir = tk.Button(ventana, text="Salir", 
                        command=ventana.quit,
                        bg="red", fg="white")
boton_salir.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()