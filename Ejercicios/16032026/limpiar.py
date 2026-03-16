ruta_in = "data/raw/crudo.txt"
ruta_out = "data/processed/procesado.txt"

datos_falsos = ["  hola\n", "MUNDO  \n", "  pYthon \n", "  ADIOS \n", "  NACIonaL \n", "  D1M \n"]
# 1. Inyectar datos en raw
with open(ruta_in, "w") as f:
    f.writelines(datos_falsos)
# 2. Pipeline de lectura y transformación
datos_limpios = []
with open(ruta_in, "r") as f:
    for linea in f.readlines():
        # Limpieza a bajo nivel
        palabra_limpia = linea.strip().lower() + "\n"
        datos_limpios.append(palabra_limpia)

# 3. Guardar en processed
with open(ruta_out, "w") as f:
    f.writelines(datos_limpios)

print("Pipeline ejecutado. Revisa la carpeta 'processed' en tu Drive.")

