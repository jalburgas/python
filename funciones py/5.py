#Función que retorna múltiples valores
def obtener_datos():
    """Retorna múltiples valores como una tupla"""
    nombre = "Carlos"
    edad = 28
    ciudad = "Barcelona"
    return nombre, edad, ciudad

# Desempaquetar los valores
nombre, edad, ciudad = obtener_datos()
print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")