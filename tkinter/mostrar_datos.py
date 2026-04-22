import tkinter as tk 

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("400x300")

etiqueta = tk.Label(ventana, text="")
etiqueta.pack(pady=50)

entrada_nonbre = tk.Entry(ventana)
entrada_nonbre.pack(pady=10)

def mostrar_datos():
    nombre = entrada_nonbre.get()
    etiqueta.config(text=f"{nombre}")   
boton = tk.Button(ventana, text="Mostrar datos", command=mostrar_datos)
boton.pack(pady=10) 
ventana.mainloop()
