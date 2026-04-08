# Menú de opciones
opcion = 0
while opcion != 3:
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Mostrar fecha")
    print("3. Salir")
    
    opcion = int(input("Selecciona una opción: "))
    
    if opcion == 1:
        print("¡Hola! ¿Cómo estás?")
    elif opcion == 2:
        print("Hoy es 23 de marzo de 2026")
    elif opcion == 3:
        print("¡Hasta luego!")
    else:
        print("Opción no válida")