import pandas as pd
import re

# Leer el archivo
with open('estrella.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Extraer información con expresiones regulares
data = []
for line in lines:
    # Buscar el patrón: [fecha hora] Click en: acción
    match = re.search(r'\[(.*?)\]\s*Click en:\s*(.*)', line)
    

    if match:
        timestamp = match.group(1)
        accion = match.group(2)
        data.append({'timestamp': timestamp, 'accion': accion})

# Crear DataFrame
df = pd.DataFrame(data)

# Convertir timestamp a datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extraer fecha y hora por separado
df['fecha'] = df['timestamp'].dt.date
df['hora'] = df['timestamp'].dt.time

# Análisis adicional
df['hora_hora'] = df['timestamp'].dt.hour
df['tiempo_entre_clicks'] = df['timestamp'].diff().dt.total_seconds()

# ===== GUARDAR EN EXCEL CON MÚLTIPLES HOJAS =====
# Usar un nombre diferente o incluir timestamp para evitar conflictos
from datetime import datetime
nombre_archivo = f'estrella_analisis_completo_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'

with pd.ExcelWriter(nombre_archivo, engine='openpyxl') as writer:
    # Hoja 1: Datos originales con todos los campos
    df.to_excel(writer, sheet_name='Datos_originales', index=False)
    
    # Hoja 2: Estadísticas por acción
    estadisticas_accion = df['accion'].value_counts().reset_index()
    estadisticas_accion.columns = ['Acción', 'Cantidad']
    estadisticas_accion.to_excel(writer, sheet_name='Estadisticas_por_accion', index=False)
    
    # Hoja 3: Acciones por fecha
    acciones_por_fecha = df.groupby('fecha')['accion'].value_counts().reset_index()
    acciones_por_fecha.columns = ['Fecha', 'Acción', 'Cantidad']
    acciones_por_fecha.to_excel(writer, sheet_name='Acciones_por_fecha', index=False)
    
    # Hoja 4: Análisis por hora
    horas_summary = df.groupby('hora_hora')['accion'].value_counts().unstack(fill_value=0)
    horas_summary_reset = horas_summary.reset_index()
    horas_summary_reset.to_excel(writer, sheet_name='Analisis_por_hora', index=False)
    
    # Hoja 5: Resumen de tiempos entre clicks
    tiempos_df = pd.DataFrame({
        'Métrica': ['Promedio (segundos)', 'Máximo (segundos)', 'Mínimo (segundos)'],
        'Valor': [
            df['tiempo_entre_clicks'].mean(),
            df['tiempo_entre_clicks'].max(),
            df['tiempo_entre_clicks'].min()
        ]
    })
    tiempos_df.to_excel(writer, sheet_name='Tiempos_entre_clicks', index=False)
    
    # Hoja 6: Secuencia completa de acciones
    secuencia = df[['timestamp', 'accion']].copy()
    secuencia['numero'] = range(1, len(secuencia) + 1)
    secuencia = secuencia[['numero', 'timestamp', 'accion']]
    secuencia.to_excel(writer, sheet_name='Secuencia_acciones', index=False)