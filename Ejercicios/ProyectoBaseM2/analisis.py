import pandas as pd

def analisis(df_ventas_clientes):

    print("Traer las personas por ciudad")
    print("Bogota")
    marcara_bogota = df_ventas_clientes["ciudad"] == "Bogota"
    df_ciudad_bogota = df_ventas_clientes[marcara_bogota]
    print(df_ciudad_bogota)


    print("Traer las personas que tengan un salario mayor a 4.000.000")
    marcara_salario = df_ventas_clientes["salario"] > 4000000
    df_salario_alto = df_ventas_clientes[marcara_salario]
    print(df_salario_alto)

    print(" \n Promedio de ventas")
    print(df_ventas_clientes["total"].mean())
    print(" \n Total de ventas ")
    print(df_ventas_clientes["total"].sum())

    print(" \n Total de ventas, por ciudad")
    ventas_por_ciudad = df_ventas_clientes.groupby('ciudad')["total"].agg(['sum', 'mean'])
    df_ventas_ordenado = ventas_por_ciudad.sort_values(by='sum', ascending=False)
    print(df_ventas_ordenado)

    