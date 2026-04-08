import tkinter as tk

ventana = tk.Tk()
ventana.title("Scrollbar")
ventana.geometry("300x200")

# Frame para contener el texto y scrollbar
frame = tk.Frame(ventana)
frame.pack(fill=tk.BOTH, expand=True)

# Text widget
texto = tk.Text(frame, wrap=tk.WORD)
texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(frame, command=texto.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Conectar scrollbar con texto
texto.config(yscrollcommand=scrollbar.set)

# Agregar texto de ejemplo
for i in range(50):
    texto.insert(tk.END, f"Línea {i+1}: Este es un texto de ejemplo\n")

ventana.mainloop()