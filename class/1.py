# Clase básica de Persona - Plantilla para crear personas
class Persona:
    nombre = ""
    edad = 0
    ciudad = ""

# Creamos el objeto estudiante
estudiante = Persona()
estudiante.nombre = "Ana García"
estudiante.edad = 25
estudiante.ciudad = "Madrid"
print(estudiante.nombre, estudiante.edad, estudiante.ciudad)

# Creamos el objeto profesor con diferentes datos
profesor = Persona()
profesor.nombre = "Carlos López"
profesor.edad = 42
profesor.ciudad = "Barcelona"
print(profesor.nombre, profesor.edad, profesor.ciudad)

# Creamos el objeto medico
medico = Persona()
medico.nombre = "Laura Martínez"
medico.edad = 35
medico.ciudad = "Valencia"
print(medico.nombre, medico.edad, medico.ciudad)
