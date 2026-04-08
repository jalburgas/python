"""Requisitos previos

Antes de ejecutar este programa, necesitas instalar las librerías necesarias:
bash

pip install mysql-connector-python"""
import tkinter as tk
from tkinter import messagebox
import mysql.connector

def probar_conexion():
    try:
        # Datos de conexión (puedes modificarlos)
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test"
        )
        
        if conexion.is_connected():
            messagebox.showinfo("Éxito", "¡Conexión establecida correctamente!")
            conexion.close()
            
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo conectar:\n{str(e)}")

# Ventana simple
ventana = tk.Tk()
ventana.title("Test MySQL")
ventana.geometry("300x150")

tk.Label(ventana, text="Prueba de Conexión a MySQL", font=("Arial", 12)).pack(pady=20)
tk.Button(ventana, text="Probar Conexión", command=probar_conexion, 
          bg="blue", fg="white", padx=20).pack(pady=20)

ventana.mainloop()