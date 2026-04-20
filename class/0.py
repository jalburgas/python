# Es una plantilla para crear objetos de forma predefinida
#permiten representar objetos o entidaes
class Auto:
    marca = ""
    modelo = 0
    placa = ""
#creamos el objeto taxi
#un objeto es un elemento de la vida real
taxi = Auto()
taxi.marca = "FIAT"
taxi.modelo = 1977
taxi.placa = "A23-555"
print(taxi.marca, taxi.modelo, taxi.placa)
# creamos el objeto patrulla con diferentes modelo, placa y marca
patrulla = Auto()
patrulla.marca = "FORD"
patrulla.modelo = 2022
patrulla.placa = "P-911-X"
print(patrulla.marca, patrulla.modelo, patrulla.placa)

