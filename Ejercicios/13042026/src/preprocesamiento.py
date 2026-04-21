import pandas as pd


def cargar_datos(ruta: str, **kwargs) -> pd.DataFrame:
    """Carga un archivo CSV en un DataFrame."""
    return pd.read_csv(ruta, **kwargs)


def manejar_valores_nulos(
    df: pd.DataFrame,
    estrategia: str = "drop",
    columnas: list[str] | None = None,
    valor_relleno=None,
) -> pd.DataFrame:
    """
    Maneja valores nulos.

    estrategias:
    - drop: elimina filas con nulos (en todas o en columnas indicadas)
    - fill: rellena nulos con un valor
    """
    if estrategia == "drop":
        if columnas:
            return df.dropna(subset=columnas)
        return df.dropna()

    if estrategia == "fill":
        if columnas:
            df = df.copy()
            df[columnas] = df[columnas].fillna(valor_relleno)
            return df
        return df.fillna(valor_relleno)

    raise ValueError("La estrategia debe ser 'drop' o 'fill'.")


def estandarizar_texto(df: pd.DataFrame, columnas: list[str]) -> pd.DataFrame:
    """Convierte texto a minúsculas y elimina espacios extra."""
    df = df.copy()
    for columna in columnas:
        if columna in df.columns:
            df[columna] = (
                df[columna]
                .astype(str)
                .str.strip()
                .str.replace(r"\s+", " ", regex=True)
                .str.lower()
            )
    return df


def limpiar_monedas(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """Elimina símbolos de moneda y convierte a numérico."""
    if columna not in df.columns:
        return df

    df = df.copy()
    df[columna] = (
        df[columna]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    df[columna] = pd.to_numeric(df[columna], errors="coerce")
    return df


def eliminar_filas_vacias(df: pd.DataFrame) -> pd.DataFrame:
    """Elimina filas completamente vacías."""
    return df.dropna(how="all")
