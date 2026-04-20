# Clase básica: Persona
#En resumen: __init__ configura automáticamente los datos iniciales de cada objeto que creas a partir de tu clase.
#self: Representa al objeto que se está creando. Es como decir "este objeto en particular".
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
 #Un método es una función que pertenece a una clase y define el comportamiento o las acciones que pueden realizar los objetos creados a partir de esa clase.       
 # El método def saludar(self): se llama método de instancia (o simplemente método).  
    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."
    
    def cumplir_anios(self):
        self.edad += 1
        return f"¡Feliz cumpleaños! Ahora tengo {self.edad} años."

# Uso de la clase
persona1 = Persona("Ana", 25)
print(persona1.saludar())  # Hola, me llamo Ana y tengo 25 años.
print(persona1.cumplir_anios())  # ¡Feliz cumpleaños! Ahora tengo 26 años.
