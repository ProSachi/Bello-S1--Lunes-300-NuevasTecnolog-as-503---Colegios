mi_lista = [300,"hola", True, 1.43]
print(mi_lista[2])

for m in mi_lista:
    print("El elemento: ", m)

print("")
mi_lista.append("nuevo")

for m in mi_lista:
    print("El elemento: ", m)

print("")
mi_lista.insert(2,"indice")

for m in mi_lista:
    print("El elemento: ", m)