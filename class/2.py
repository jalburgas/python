#Clase Perro
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau guau!"
    
    def cumplir_anios(self):
        self.edad += 1
        return f"{self.nombre} ahora tiene {self.edad} años"

# Usar la clase
mi_perro = Perro("Max", 3)
print(mi_perro.ladrar())        # Max dice: ¡Guau guau!
print(mi_perro.cumplir_anios()) # Max ahora tiene 4 años