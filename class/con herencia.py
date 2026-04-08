class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
    
    def encender(self):
        self.encendido = True
        return f"{self.marca} {self.modelo} encendido."
    
    def apagar(self):
        self.encendido = False
        return f"{self.marca} {self.modelo} apagado."

class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas
        self.velocidad = 0
    
    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            return f"Acelerando a {self.velocidad} km/h"
        return "Primero debes encender el coche."
    
    def frenar(self):
        self.velocidad = max(0, self.velocidad - 10)
        return f"Frenando. Velocidad actual: {self.velocidad} km/h"

# Uso de la clase
mi_coche = Coche("Toyota", "Corolla", 4)
print(mi_coche.encender())  # Toyota Corolla encendido.
print(mi_coche.acelerar(30))  # Acelerando a 30 km/h
print(mi_coche.frenar())  # Frenando. Velocidad actual: 20 km/h