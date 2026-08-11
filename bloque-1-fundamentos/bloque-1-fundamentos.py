#Presentación

"""nombre = "Aitor"
edad = 39
profesion = "Quiromasajista"

print(f"Me llamo {nombre}, tengo {edad} años y soy {profesion}." )

#Obtener número mayor de 18 de una lista.

#entrada
edades = [12, 25, 17, 39, 14, 21]

#Proceso
edades_mayores = []


for edad in edades:    
    if edad > 18:
        edades_mayores.append(edad)
#salida
print(edades_mayores)

#obtener dos listas, moyor que 5 y menor o igual a 5

#entrada
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
print(mayores, menores_o_iguales)

#obtener tres listas, par, impar y negativo de una lista de números.
#entrada
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
print(f"{par}\n{impar}\n{negativo}")
    
#obtener la suma de todos los números mayores que 10 de una lista.
#entrada
numeros =  [3, 8, 12, 5, 20, 7, 2, 15]

#proceso
suma = 0
for num in numeros:
    if num > 10:
        suma += num

#salida
print(suma)

#Queremos calcular la suma de los números pares mayores que 10.
#entrada
numeros = [4, 12, 7, 20, 3, 18, 11, 6]

#proceso
suma = 0
for num in numeros:
    if num % 2 == 0 and num > 10:
        suma += num

#salida
print(suma)

#Queremos obtener una lista con los nombres que tengan más de 4 caracteres y empiecen por "A".
#entrada
nombres = ["Ana", "Carlos", "Aitor", "Bea", "Alberto", "Luis"]

#proceso
filtrado = []
for nombre in nombres:
    if len(nombre) > 4 and nombre.startswith("A"):
        filtrado.append(nombre)

#salida
print(filtrado)

#Queremos encontrar cuántas frases contienen la palabra "Python".
#entrada
frases = [
    "Hola mundo",
    "Python es genial",
    "Me gusta programar",
    "Hola Python",
    "Estoy aprendiendo"
]
#proceso
suma = 0
for py in frases:
    if py.count("Python") >= 1:
        suma += 1

#salida
print(suma)


#Queremos obtener 3 variables con, los numeros mayores a 10, la cantidad de esos números y la suma de todos.
#entrada
numeros = [4, 12, 7, 20, 3, 18, 11, 6, 25, 2]

#datos
numeros_mayores = []
cantidad = 0
suma = 0

#Proceso
for num in numeros:
    if num > 10:
        numeros_mayores.append(num)
        cantidad += 1
        suma += num

#Salida
print(f"Los números son:{numeros_mayores}\nLa cantidad de los úmeros: {cantidad}\nLa suma de esos números son: {suma}")

#Positivos, negativos, ceros, y suma de positivos y negativos.
#Entrada
numeros = [5, -3, 0, 8, -7, 12, 0, -2, 4, -9]

#Datos
positivo = []
negativos = []
cantidad_ceros = 0
suma_positivos = 0
suma_negativos = 0

#Proceso
for num in numeros:
    if num > 0:
        positivo.append(num)
        suma_positivos += num
    elif num == 0:
        cantidad_ceros += 1
    else:
        negativos.append(num)
        suma_negativos += num

#Salida
print(f"positivos: {positivo}\nNegativos: {negativos}\ncantidad de ceros: {cantidad_ceros}\nSuma de positivos {suma_positivos}\nSuma negativos: {suma_negativos}")

#Lista de palabras, filtrar palabras mayores de 5 caracteres, cantidad de palabras, y cantidad de las palabras.
#Entrada
palabras = ["sol", "programacion", "casa", "python", "ordenador", "IA", "codigo"]

#Datos
mayores_5 = []
cantidad = 0
longitud_total = 0

#proceso
for palabra in palabras:
    if len(palabra) > 5:
        mayores_5.append(palabra)
        cantidad += 1
        longitud_total += len(palabra)

print(f"{mayores_5}\n{cantidad}\n{longitud_total}")

#Datos que no deberían cambiar
#entrada
persona = ("Aitor", 39, "Barcelona", "Quiromasajista")

#datos
nombre = persona[0]
edad = persona[1]
ciudad = persona[2]
profesion = persona[3]

#salida
print(f"nombre: {nombre}\nEdad: {edad}\nCiudad: {ciudad}\nProfesión: {profesion}")

#Recorrer una tupla
frutas = ("manzana", "pera", "plátano", "naranja", "kiwi")

for fruta in frutas:
    print(fruta)

#Tupla + condición + contador
edades = (12, 25, 17, 39, 14, 21, 18, 9)

#Proceso
mayores = 0
for edad in edades:
    if edad >= 18:
        mayores += 1

#salida
print(mayores)"""

#Tupla + condición + acumulador
#entrada
precios = (12.50, 8.75, 20.00, 5.50, 15.25, 30.00)

#datos
suma_total = 0

#proceso
for precio in precios:
    if precio > 10:
        suma_total += precio

#salida
print(suma_total)