import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# 1. Consumir la API
url = "https://69f91db8c509a40d3aa236e3.mockapi.io/api/v1/evento"
response = requests.get(url)

# 2. Verificar que la petición fue exitosa (código 200)
if response.status_code == 200:
    # 3. Convertir a JSON
    data = response.json()
    
    # 4. Convertir a DataFrame de Pandas
    # Si los datos están anidados, usa pd.json_normalize(data)
    df = pd.DataFrame(data)
    
    # Mostrar las primeras filas
    print(df.head())
else:
    print(f"Error al consumir la API: {response.status_code}")


print("--- GRÁFICO 1: TENDENCIA TEMPORAL (Líneas) ---")
plt.figure(figsize=(8, 4))
# marker='o' pone un punto en cada mes
plt.plot(df['name'], df['id'], color='#2ca02c', marker='x', linewidth=2)
plt.title("Usuarios con ID)", fontsize=14, fontweight='bold')
plt.xlabel("Nombres")
plt.ylabel("ID")
plt.show() # Cierra y renderiza el primer gráfico