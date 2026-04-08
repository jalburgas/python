#Información de una canción 
# Programa que solicita al usuario
#  el nombre de una canción y su artista, 
# y luego muestra esta información junto con un género musical predefinido.

#//////////////////////////////////////////////////////////
# Constante
# el = es para asignar un valor a una variable, en este caso a la constante GENERO
GENERO = "Pop"

# Variables
cancion = input("¿Qué canción te gusta? ")
artista = input("¿Quién la canta? ")
#imprime el valor de la variable cancion directamente sin formato
print (cancion)
# Impresión
print(f"\nCanción: {cancion}")
print(f"Artista: {artista}")
print(f"Género: {GENERO}")
#/////////////////////////////////////////////////////////
print ("Ejemplo de impresión sin formato aqui solo muestra el texto literal cancion en lugar del valor de la variable cancion")
#Ejemplo de impresión sin formato aqui solo muestra el texto literal "cancion" en lugar del valor de la variable cancion
print("Canción: cancion")

#Es un f-string (formatted string literal) que combina:

#    \n: salto de línea

#    {cancion}: variable insertada dentro del string