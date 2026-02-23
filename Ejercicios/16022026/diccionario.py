diccionario = {"fisica":3,"matematicas":4,"Español":4.5}

for clave, valor in diccionario.items():
    print(f"Materia: {clave} -> Nota: {valor}")

print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())

print(diccionario.get("Fisica","Valor no Encontrado"))