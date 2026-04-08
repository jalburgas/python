#Proyecto: Lista de tareas simple
import tkinter as tk

def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)

def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion)

ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("300x400")

# Frame superior para entrada
frame_superior = tk.Frame(ventana)
frame_superior.pack(pady=10)

entrada_tarea = tk.Entry(frame_superior, width=30)
entrada_tarea.pack(side=tk.LEFT, padx=5)

boton_agregar = tk.Button(frame_superior, text="Agregar", command=agregar_tarea)
boton_agregar.pack(side=tk.LEFT)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, height=15, width=40)
lista_tareas.pack(pady=10)

# Botón eliminar
boton_eliminar = tk.Button(ventana, text="Eliminar seleccionada", 
                          command=eliminar_tarea)
boton_eliminar.pack()

ventana.mainloop()