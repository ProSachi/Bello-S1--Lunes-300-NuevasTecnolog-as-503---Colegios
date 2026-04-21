# Aplicacion de Analisis de Datos (Momento 2)

Proyecto en Python para cargar, limpiar y analizar datos con Pandas.

## Estructura

- `analisis.py`: script principal con preguntas de analisis.
- `src/preprocesamiento.py`: funciones de carga y limpieza.
- `data/clientes.csv` y `data/ventas.csv`: datos relacionados para merge.
- `requirements.txt`: dependencias.

## Que se hace en el proyecto

- Carga de datos desde CSV.
- Manejo de valores nulos.
- Estandarizacion de texto (minusculas y espacios).
- Limpieza especifica de moneda (`monto`).
- Operaciones de filtrado, merge y groupby.

## Configuracion de entorno virtual (venv)

En PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ejecucion

```powershell
python analisis.py
```

El script imprime en consola:
1. Elemento con mayor frecuencia de registros.
2. Metrica agregada por categoria (unidades por bodega).
3. Conteo por condicion especifica (envios retrasados).

## Conceptos clave para sustentacion

- **DataFrame**: estructura tabular de Pandas (filas y columnas) para analizar datos.
- **Entorno virtual**: permite aislar dependencias del proyecto y evitar conflictos con otros proyectos.
