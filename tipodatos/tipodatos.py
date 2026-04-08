# CONSTANTES
TITULO = "📊 APRENDIENDO TIPOS DE DATOS 📊"

print(TITULO)
print("="*40)

# Ingresando diferentes tipos de datos
print("\n1. DATO TIPO TEXTO (str)")
nombre = input("   Escribe tu nombre: ")

print("\n2. DATO TIPO NÚMERO ENTERO (int)")
edad = int(input("   Escribe tu edad (solo números): "))

print("\n3. DATO TIPO NÚMERO DECIMAL (float)")
precio = float(input("   Escribe un precio (ejemplo: 19.99): "))

print("\n4. DATO TIPO BOOLEANO (bool)")
respuesta = input("   ¿Te gusta Python? (si/no): ")
le_gusta = respuesta.lower() == "si"

print("\n" + "="*40)
print("📌 RESULTADOS Y SUS TIPOS")
print("="*40)

# Mostrando cada dato con su tipo
print(f"\n📝 Nombre: {nombre}")
print(f"   → Tipo: {type(nombre)} (String/Texto)")

print(f"\n🔢 Edad: {edad}")
print(f"   → Tipo: {type(edad)} (Integer/Entero)")

print(f"\n💰 Precio: ${precio}")
print(f"   → Tipo: {type(precio)} (Float/Decimal)")

# Línea corregida: eliminado "juan" que causaba el error
print(f"\n❤️ ¿Te gusta Python?: {le_gusta}")
print(f"   → Tipo: {type(le_gusta)} (Boolean/Verdadero o Falso)")

print("\n" + "="*40)
print("🎯 RESUMEN DE TIPOS DE DATOS")
print("="*40)
print("• str  → Texto (se escribe entre comillas)")
print("• int  → Números enteros (sin punto decimal)")
print("• float → Números decimales (con punto)")
print("• bool → Valores True o False")