from multiplicar import multiplicar
from dividir import dividir
def restar(a, b):
    return a-b



acumulador= []
condicion=True
while(condicion):
    print("Cargando calculadora....")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = int(input("Ingresa el numero de la operación a realizar:"))
    if(opcion!=5):
        numero1 = float(input("Dame un numero"))
        numero2 = float(input("Dame otro numero"))
    match opcion:
        case 1:
            print(f"La suma es: {(numero1+numero2)}")
            acumulador.append(numero1+numero2) 
        case 2:
            print(f"La resta es: {restar(numero1, numero2)}")
            acumulador.append((restar(numero1, numero2))) 
        case 3:
            print(f"La Multiplicaicón es: {multiplicar(numero1, numero2)}")
            acumulador.append((multiplicar(numero1, numero2)))
        case 4:
            print(f"La división es: {dividir(numero1, numero2)}")
            acumulador.append((dividir(numero1, numero2))) 
        case 5: 
            print("Saliendo de la calculadora")
            condicion = False
        
    print(len(acumulador))
    print(*acumulador, sep='\n')

