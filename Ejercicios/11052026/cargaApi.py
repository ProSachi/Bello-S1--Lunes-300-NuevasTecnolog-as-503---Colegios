import requests
import pandas as pd

def obtener_datos_enfermeros():
    """
    Obtiene los datos de enfermeros desde la API y retorna un DataFrame.
    
    Returns:
        pd.DataFrame: DataFrame con los datos de enfermeros
    """
    # URL de la API
    url = 'https://6a023c250d92f63dd2537110.mockapi.io/api/v3/objeto'
    
    # Realizar la petición GET
    response = requests.get(url)
    
    # Verificar si la petición fue exitosa
    if response.status_code == 200:
        # Convertir la respuesta a JSON
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error: {response.status_code}")
        return None

# Si ejecutas este archivo directamente, muestra los datos
if __name__ == "__main__":
    df = obtener_datos_enfermeros()
    if df is not None:
        print(df.head())