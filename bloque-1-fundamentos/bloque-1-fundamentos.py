#Presentación

"""nombre = "Aitor"
edad = 39
profesion = "Quiromasajista"

print(f"Me llamo {nombre}, tengo {edad} años y soy {profesion}." )
"""
#Obtener número mayor de 18 de una lista.

#entrada
"""edades = [12, 25, 17, 39, 14, 21]

#Proceso
edades_mayores = []


for edad in edades:    
    if edad > 18:
        edades_mayores.append(edad)
#salida
print(edades_mayores)"""

#obtener dos listas, moyor que 5 y menor o igual a 5

"""#entrada
edades = [4, 15, 7, 22, 33, 18, 9]

#Proceso
mayores = []
menores_o_iguales = []


for edad in edades:    
    if edad > 5:
        mayores.append(edad)
    else:
        menores_o_igual.append(edad)
#salida
print(mayores, menores_o_iguales)"""

#obtener tres listas, par, impar y negativo de una lista de números.
"""#entrada
numeros = [4,-15, 7, -22, 33, -18, 9, -10, -3]

#proceso
par = []
impar = []
negativo = []

for num  in numeros:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

    if num < 0:
        negativo.append(num)
#salida
print(f"{par}\n{impar}\n{negativo}")"""
    
#obtener la suma de todos los números mayores que 10 de una lista.
"""#entrada
numeros =  [3, 8, 12, 5, 20, 7, 2, 15]

#proceso
suma = 0
for num in numeros:
    if num > 10:
        suma += num

#salida
print(suma)"""

#Queremos calcular la suma de los números pares mayores que 10.
"""#entrada
numeros = [4, 12, 7, 20, 3, 18, 11, 6]

#proceso
suma = 0
for num in numeros:
    if num % 2 == 0 and num > 10:
        suma += num

#salida
print(suma)"""

#Queremos obtener una lista con los nombres que tengan más de 4 caracteres y empiecen por "A".
#entrada
"""nombres = ["Ana", "Carlos", "Aitor", "Bea", "Alberto", "Luis"]

#proceso
filtrado = []
for nombre in nombres:
    if len(nombre) > 4 and nombre.startswith("A"):
        filtrado.append(nombre)

#salida
print(filtrado)"""

#Queremos encontrar cuántas frases contienen la palabra "Python".
frases = [
    "Hola mundo",
    "Python es genial",
    "Me gusta programar",
    "Hola Python",
    "Estoy aprendiendo"
]
suma = 0
for py in frases:
    if py.count("Python") >= 1:
        suma += 1

print(suma)