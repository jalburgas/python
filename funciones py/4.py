#Función con parámetros por defecto
def crear_usuario(nombre, rol="usuario", activo=True):
    """Función que crea un usuario con parámetros opcionales"""
    return {
        "nombre": nombre,
        "rol": rol,
        "activo": activo
    }

# Diferentes formas de llamar
usuario1 = crear_usuario("Carlos")
usuario2 = crear_usuario("María", "admin")
usuario3 = crear_usuario("Luis", activo=False)

print(usuario1)
print(usuario2)
print(usuario3)