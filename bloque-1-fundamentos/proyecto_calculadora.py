#Calculadora básica
#siguiente paso, controlar entrada, por si usuario introduce digito en vez de un número.

#entrada
print("Introduce el primer número:")
numero_1 = int(input())
print("Introduce el operado: +, -, / o *: ")
operador = input()
print("Por último, introduce el segundo número: ")
numero_2 = int(input())
#datos
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
    print(sumar(numero_1, numero_2))
elif operador == "-":
    print(restar(numero_1, numero_2))
elif operador == "/":
    print(dividir(numero_1, numero_2))
elif operador == "*":
    print(multiplicar(numero_1, numero_2))










