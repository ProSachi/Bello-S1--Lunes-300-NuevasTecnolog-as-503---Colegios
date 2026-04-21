import pandas as pd

def carga_clientes():
    df_archivo = pd.read_csv('data/raw/cliente.csv')
    df_archivo.info()
    return df_archivo

def carga_ventas():
    df_ventas = pd.read_csv('data/raw/ventas.csv')
    df_ventas.info()
    return df_ventas





