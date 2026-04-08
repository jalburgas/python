#¿Cuándo usar tuplas?

 #   Cuando necesitas datos que no deben cambiar

  #  Para claves de diccionarios

   # Para retornar múltiples valores de una función

    #Cuando la inmutabilidad mejora la seguridad del código

    #Son más eficientes en memoria que las listas
# Tupla vacía
tupla_vacia = ()
print(tupla_vacia)  # ()

# Tupla con un solo elemento (¡importante la coma!)
tupla_un_elemento = (5,)  # Sin la coma sería un entero
print(tupla_un_elemento)  # (5,)

# Tupla con múltiples elementos
colores = ("rojo", "verde", "azul")
print(colores)  # ('rojo', 'verde', 'azul')

# Tupla sin paréntesis (tuple packing)
coordenadas = 10, 20, 30
print(coordenadas)  # (10, 20, 30)

