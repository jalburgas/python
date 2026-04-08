import tkinter as tk  # Importamos la biblioteca tkinter para crear interfaces gráficas

def tecla_presionada(event):
    """Función que se ejecuta cuando se presiona una tecla en el área sensible"""
    # event.keysym contiene el nombre de la tecla presionada (ej: 'a', 'Return', 'space')
    # Actualizamos la etiqueta con la información de la tecla presionada
    etiqueta.config(text=f"Tecla presionada: {event.keysym}")

def clic_raton(event):
    """Función que se ejecuta cuando se hace clic izquierdo en el área sensible"""
    # event.x y event.y son las coordenadas del clic dentro del frame
    # Actualizamos la etiqueta con las coordenadas donde se hizo clic
    etiqueta.config(text=f"Clic en posición: ({event.x}, {event.y})")

def mover_raton(event):
    """Función que se ejecuta cuando se mueve el mouse sobre el área sensible"""
    # event.x y event.y se actualizan continuamente con la posición actual del mouse
    # Actualizamos una etiqueta diferente para mostrar la posición en tiempo real
    coordenadas.config(text=f"Posición: ({event.x}, {event.y})")

# Creamos la ventana principal
ventana = tk.Tk()  # Tk() crea la ventana raíz de la aplicación
ventana.title("Eventos")  # Establecemos el título que aparecerá en la barra de título
ventana.geometry("400x300")  # Definimos el tamaño inicial de la ventana (ancho x alto)

# Crear área sensible - un Frame que actuará como zona interactiva
area = tk.Frame(ventana, width=400, height=200, bg="lightgray")
# Parámetros del Frame:
# - ventana: contenedor padre donde se colocará el frame
# - width/height: dimensiones del área sensible (400x200 píxeles)
# - bg: color de fondo (gris claro para hacer visible el área)
area.pack(pady=20)  # pack() coloca el frame en la ventana con margen superior/inferior de 20px

# Vincular eventos al área sensible:
# <Key> - Se activa cuando se presiona cualquier tecla (solo funciona si el widget tiene el foco)
area.bind("<Key>", tecla_presionada)

# <Button-1> - Se activa con clic izquierdo del mouse (Button-2 sería clic central, Button-3 clic derecho)
area.bind("<Button-1>", clic_raton)

# <Motion> - Se activa continuamente cuando el mouse se mueve dentro del widget
area.bind("<Motion>", mover_raton)

# focus_set() da el foco al frame para que pueda recibir eventos de teclado
# Sin esto, las teclas presionadas no activarían el evento <Key>
area.focus_set()

# Creamos una etiqueta para mostrar mensajes principales
etiqueta = tk.Label(ventana, text="Presiona una tecla o haz clic")
# Parámetros: ventana (contenedor) y text (texto inicial a mostrar)
etiqueta.pack()  # pack() coloca la etiqueta debajo del frame

# Creamos otra etiqueta específica para mostrar las coordenadas del mouse en tiempo real
coordenadas = tk.Label(ventana, text="Posición: ")
coordenadas.pack()  # Colocamos esta etiqueta debajo de la anterior
ventana.mainloop()