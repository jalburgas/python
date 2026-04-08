# Sumar números hasta alcanzar 100
suma = 0
numero = 1
while suma < 100:
    suma += numero
    print(f"Sumando {numero}, suma actual: {suma}")
    numero += 1
print(f"¡Se alcanzó {suma}!")