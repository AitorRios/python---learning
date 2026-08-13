#Presentación

nombre = "Aitor"
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
        menores_o_iguales.append(edad)
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
print(mayores)

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

#Dia 2 Diccionarios + bucles + condiciones
# tambien, conteo y calculos.
#entrada
notas = {
    "Ana": 8,
    "Luis": 5,
    "Marta": 9,
    "Pedro": 4,
    "Laura": 7
}

#datos
aprobado = 0
suspendidos = 0
suma_notas = 0

#proceso
for nombre, nota in notas.items():
    if nota >= 5:
        print(f"{nombre}: {nota} - Aprobado")
        aprobado += 1
        suma_notas += nota
    else:
        print(f"{nombre}: {nota} - Suspendido")
        suspendidos += 1
        suma_notas += nota

nota_media = suma_notas / len(notas)
#salida
print(f"Aprobados: {aprobado}.\nSuspendidos: {suspendidos}.\nNota media: {nota_media:.2f}.")

#diccionarios + bucles + condicionales + contadores
#entrada
productos = {
    "Pan": 1.20,
    "Leche": 0.95,
    "Huevos": 2.50,
    "Cafe": 4.80,
    "Arroz": 1.70,
    "Carne": 7.50
}

#datos
producto_encontrados =[] #contendeor
cuantos_productos = 0 #contador
suma_total = 0   #acumulador

#proceso
for key, valor in productos.items():
    if valor > 2:
        producto_encontrados.append(key)
        cuantos_productos += 1
        suma_total += valor

#salida
print(f"Productos encontrados: {producto_encontrados}\nCantidad de productos: {cuantos_productos}\n"
      f"Valor total: {suma_total}"
)

# siguiente ejercicio
#entrada
notas = {
    "Ana": 8,
    "Luis": 5,
    "Marta": 9,
    "Pedro": 4,
    "Laura": 7
}
# datos
suma_total = 0  #acumulado
que_alumnos = [] #contenedor
cuantos_alumnos = 0 #contador

#proceso
for valor in notas.values():
    suma_total += valor

nota_media = suma_total / len(notas)

for alumno, nota in notas.items():
    if nota > nota_media:
        que_alumnos.append(alumno)
        cuantos_alumnos += 1

#salida
print(f"nota media: {nota_media}\nalumnos que estan por encima de la nota media: {que_alumnos}\n"
      f"cuantos alumnos: {cuantos_alumnos}"
)

# por último las funciones
#crea una función llamada presentacion() que imprima:
def presentacion():
    print("Estoy aprendiendo Python")

presentacion()

#Crea una función llamada saludar_persona que reciba un nombre y muestre:
def saludar_persona(nombre): #nombre es el parámetro
    print(f"Hola {nombre}")

saludar_persona("Aitor") #En este caso "aitor", "Silvia. etc. serían los argumentos que pasamos a la función"
saludar_persona("Silvia")
saludar_persona("Marta")

#Crea una función llamada calcular_doble que: reciba un número como parámetro .devuelva (return) el doble de ese número  después guarda el resultado en una variable y muéstralo con print()
def calcular_doble(numero):
    doble = numero * 2 #La variable esta bien, pero en return tambien se puden hacer operaciones directas.
    return doble #return devuelve el valor para poder utilizarlo fuera de la función

doblar = calcular_doble(3)
print(doblar)

#siguiente return + condición
def es_mayor_de_edad(edad):
    if edad >= 18:
        return "Mayor de edad"
    else:
        return "Menor de edad"

resultado = es_mayor_de_edad(16)
print(resultado)

# recibir dos parámetros 
def calcular_precio_final (precio, descuento):
    return precio - (precio * descuento / 100) #Lo comentado mas arriba, no es obligatorio variables, tambien se pueden hacer directo en return
    
resultado_final = calcular_precio_final(100, 20)
print(resultado_final)

#debe recibir tres notas y devolver la media.
def calcular_media (nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3 # Python sigue las mismas reglas de prioridad de operaciones que las matemáticas

nota_media = calcular_media(7, 8, 9)
print(nota_media)

#Debe devolver: "Suspenso" si la nota es menor que 5. "Aprobado" si es 5 o más. Después prueba con 3 notas diferentes.
def nota_final(nota):
    if nota < 5:
        return "Suspenso"
    else:
        return "Aprobado" 

print(nota_final(8))
print(nota_final(4))
print(nota_final(6))
#Una función no tiene por qué devolver números. Puede devolver: números → return 8. texto → return "Aprobado". valores booleanos → return True. listas → return [1, 2, 3] etc.
#Y luego puedes utilizar ese valor donde quieras.