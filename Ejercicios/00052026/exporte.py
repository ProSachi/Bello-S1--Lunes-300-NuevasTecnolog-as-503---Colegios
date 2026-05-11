import matplotlib.pyplot as plt
from cargaApi import obtener_datos_enfermeros

# Obtener los datos desde la API
df = obtener_datos_enfermeros()

if df is not None:
    print("Datos cargados exitosamente:")
    print(df.head())
    print(f"\nColumnas disponibles: {df.columns.tolist()}")
    print(f"Total de registros: {len(df)}")

# 1. Creamos un gráfico de prueba

plt.figure(figsize=(10, 8))
colores=['blue','orange','green']
plt.barh(df['name'], df['stock'], color=colores, edgecolor='black', linewidth=0.7)
plt.xlabel('Stock (Unidades)', fontsize=12, fontweight='bold')
plt.ylabel('Productos', fontsize=12, fontweight='bold')
plt.title("Reporte de Producción")
plt.ylabel("Unidades")
plt.xticks(rotation=45)


# ==========================================
# EL BLOQUE DE EXPORTACIÓN (Antes del show)
# ==========================================

# Parámetro clave transversal: bbox_inches='tight'
# Obliga a Matplotlib a calcular el "Bounding Box" (la caja de la imagen) 
# abrazando todos los textos. Si no lo pones, los títulos largos o las 
# etiquetas rotadas del eje X quedarán cortadas por la mitad en la foto final.

# Opción A: PNG (Rasterizado / Mapa de Bits)
# Ideal para: PowerPoint, Word, correos electrónicos o impresión física.
# Parámetro técnico: dpi=300 (Puntos por pulgada). Es el estándar internacional 
# para calidad de imprenta. Si omites el DPI, se guardará a 72 o 100 DPI (se verá borroso).
plt.savefig("reporte_impresion.png", format='png', dpi=300, bbox_inches='tight')

# Opción B: SVG (Vectorial / Matemático)
# Ideal para: Páginas web, aplicaciones interactivas o diseño gráfico (Illustrator/Figma).
# No usa DPI porque no está hecho de píxeles, sino de fórmulas matemáticas. 
# Puedes hacerle zoom infinito sin que se pixele.
plt.savefig("reporte_web.svg", format='svg', bbox_inches='tight')

# Opción C: PDF (Vectorial Empaquetado)
# Ideal para: Informes formales, adjuntos gerenciales o entregables académicos.
# Al igual que el SVG, el PDF guarda los gráficos de forma vectorial, garantizando
# texto nítido sin importar cuánto zoom haga el gerente.
plt.savefig("reporte_ejecutivo.pdf", format='pdf', bbox_inches='tight')

# ==========================================
# RENDERIZADO FINAL
# ==========================================
plt.show() # Ahora sí, mostramos en pantalla y vaciamos la memoria.
