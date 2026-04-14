numero_secreto = 7
intentos = 0

while True:  # Bucle infinito
    intento = int(input("Adivina el número (1-10): "))
    intentos += 1
    
    if intento == numero_secreto:
        print(f"¡Correcto! Lo lograste en {intentos} intentos.")
        break  # Sale del bucle cuando acierta
    else:
        print("Incorrecto, intenta de nuevo.")
