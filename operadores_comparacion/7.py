#Menor o igual que (<=) - ¿Es más pequeño o igual?
# ¿Tu estatura te permite subir al juego? (máximo 150 cm)
mi_altura = 140
altura_maxima = 150
print(mi_altura <= altura_maxima)  # True (sí, eres más bajo)

# ¿Mides justo 150?
mi_altura = 150
print(mi_altura <= altura_maxima)  # True (sí, es igual)

# ¿Eres muy alto con 160?
mi_altura = 160
print(mi_altura <= altura_maxima)  # False (no, te pasas)
