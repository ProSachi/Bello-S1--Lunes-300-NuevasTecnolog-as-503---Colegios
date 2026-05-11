import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({
    'categoria': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'valor': [320, 450, 280, 510, 390] })
listaColores = ['blue', 'red', 'green']
# 1. Preparar el lienzo (Ancho, Alto en pulgadas)
plt.figure(figsize=(10, 6))
# 2. Pintar el gráfico (usando la integración directa de Pandas)
df.plot(kind='bar', x='categoria', y='valor', color=listaColores)
# 3. Personalización y Contexto (Metadata)
plt.title("Título Claro y de Negocio", fontsize=14)
plt.xlabel("Etiqueta del Eje X")
plt.ylabel("Etiqueta del Eje Y")
plt.xticks(rotation=45) # Rotar textos para que no colisionen
# 4. Renderizar (Mostrar a pantalla)
plt.show()
