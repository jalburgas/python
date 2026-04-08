#Acceso a elementos
frutas = ("manzana", "banana", "cereza", "durazno")

# Acceso por índice (empieza en 0)
print(frutas[0])     # manzana
print(frutas[2])     # cereza

# Índices negativos (desde el final)
print(frutas[-1])    # durazno (último)
print(frutas[-2])    # cereza (penúltimo)

# Slicing (rebanado)
print(frutas[1:3])   # ('banana', 'cereza')
print(frutas[:2])    # ('manzana', 'banana')
print(frutas[2:])    # ('cereza', 'durazno')