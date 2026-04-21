import pandas as pd

from src.preprocesamiento import (
    cargar_datos,
    eliminar_filas_vacias,
    estandarizar_texto,
    limpiar_monedas,
    manejar_valores_nulos,
)


def preparar_datos():
    clientes = cargar_datos("data/clientes.csv")
    ventas = cargar_datos("data/ventas.csv")

    # Limpieza base
    clientes = eliminar_filas_vacias(clientes)
    ventas = eliminar_filas_vacias(ventas)

    # Estandarizar columnas de texto
    clientes = estandarizar_texto(clientes, ["nombre", "ciudad"])
    ventas = estandarizar_texto(ventas, ["producto", "estado_envio", "bodega"])

    # Limpieza específica de montos
    ventas = limpiar_monedas(ventas, "monto")

    # Manejo de nulos
    clientes = manejar_valores_nulos(clientes, estrategia="drop", columnas=["cliente_id", "nombre"])
    ventas = manejar_valores_nulos(
        ventas,
        estrategia="drop",
        columnas=["venta_id", "cliente_id", "producto", "cantidad", "monto"],
    )

    # Convertir tipos
    clientes["cliente_id"] = pd.to_numeric(clientes["cliente_id"], errors="coerce")
    ventas["cliente_id"] = pd.to_numeric(ventas["cliente_id"], errors="coerce")
    ventas["cantidad"] = pd.to_numeric(ventas["cantidad"], errors="coerce")

    clientes = clientes.dropna(subset=["cliente_id"])
    ventas = ventas.dropna(subset=["cliente_id", "cantidad", "monto"])

    clientes["cliente_id"] = clientes["cliente_id"].astype(int)
    ventas["cliente_id"] = ventas["cliente_id"].astype(int)

    return clientes, ventas


def responder_preguntas(clientes: pd.DataFrame, ventas: pd.DataFrame):
    # Merge
    df = ventas.merge(clientes, on="cliente_id", how="inner")

    # 1) Frecuencia: producto con mayor número de transacciones
    top_producto = df["producto"].value_counts().idxmax()
    top_producto_count = df["producto"].value_counts().max()

    # 2) Agregación: total de unidades por bodega
    unidades_por_bodega = (
        df.groupby("bodega", as_index=False)["cantidad"]
        .sum()
        .sort_values("cantidad", ascending=False)
    )

    # 3) Filtrado + conteo: envíos retrasados
    retrasados = df[df["estado_envio"] == "retrasado"].shape[0]

    print("=== RESPUESTAS DEL ANALISIS ===")
    print(
        f"1. Producto con mayor cantidad de registros: '{top_producto}' con {top_producto_count} transacciones."
    )

    print("\n2. Total de unidades por bodega:")
    print(unidades_por_bodega.to_string(index=False))

    print(f"\n3. Cantidad de envios en estado 'retrasado': {retrasados}")


if __name__ == "__main__":
    clientes_df, ventas_df = preparar_datos()
    responder_preguntas(clientes_df, ventas_df)
