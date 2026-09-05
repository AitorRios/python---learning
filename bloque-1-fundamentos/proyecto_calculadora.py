#Calculadora básica
#siguiente paso, hacer que imprima en int cuando sea necesario y en float cuando lleve decimales.
#entrada

operadores_correctos = ["+", "-", "/", "*"]
while True:
    try:
        numero_1 = float(input("Introduce el primer número:"))
        while True:
            operador = input("Introduce el operado: +, -, / o *:")
            if operador not in operadores_correctos:
                print("Introduce uno de los operaores correctos")
            else:
                break
        while True:            
            try:
                numero_2 = float(input("Por último, introduce el segundo número: "))
                break
            except ValueError:
                print("Introduce un valor númerico correcto")
        break
    except ValueError:
        print("Introduce un valor númerico correcto")

def sumar(numero1, numero2):
    return numero1 + numero2


def restar(numero1, numero2):
    return numero1 - numero2


def dividir(numero1, numero2):
    return numero1 / numero2


def multiplicar(numero1, numero2):
    return numero1 * numero2

#proceso
if operador == "+":
    suma = sumar(numero_1, numero_2)
    if suma % 1 == 0:
        print(int(suma))
    else:
        print(suma)
elif operador == "-":
    resta = restar(numero_1, numero_2)
    if resta % 1 == 0:
        print(int(resta))
    else:
        print(resta)
elif operador == "/":
    divi = dividir(numero_1, numero_2)
    if divi % 1 == 0:
        print(int(divi))
    else:
        print(divi)
elif operador == "*":
    multiplica = multiplicar(numero_1, numero_2)
    if multiplica % 1 == 0:
        print(int(multiplica))
    else:
        print(multiplica)

