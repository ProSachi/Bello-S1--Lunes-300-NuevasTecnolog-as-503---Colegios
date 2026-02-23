nombre = input("Dame tu nombre")
lista = [input("Dame un hobbie"), input("Dame un hobbie"), input("Dame un hobbie")]

diccionario = {"nombre":nombre,"hobbie1":lista[0], "hobbie2":lista[1], "hobbie3":lista[2]}

for clave, valor in diccionario.items():
    print(f"La clave es {clave} y el valor es {valor}")