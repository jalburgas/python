#Validación de entrada de usuario
# Solicitar un número positivo
numero = -1
while numero < 0:
    numero = int(input("Ingresa un número positivo: "))
    if numero < 0:
        print("Error: El número debe ser positivo.")
print(f"¡Correcto! Ingresaste: {numero}")