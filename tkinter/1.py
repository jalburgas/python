import tkinter as tk

#Tk() es la clase que representa la ventana raíz
ventana = tk.Tk()
ventana.title("Mi primera ventana")
#Define el tamaño de la ventana Formato: "ancho x alto" (en píxeles)
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="¡Tkinter funciona!")
#pack() es un "gestor de geometría" que organiza los elementos
#pady=50 añade espacio vertical (padding) arriba y abajo de 50 píxeles
#Esto centra la etiqueta verticalmente en la ventana
etiqueta.pack(pady=50)

ventana.mainloop()
    # ¡Muy importante! Inicia el bucle principal de la aplicación
    # Mantiene la ventana abierta y espera a que el usuario interactúe
    # Sin esta línea, la ventana aparecería y se cerraría inmediatamente
    # Es como el "motor" que mantiene viva la aplicación