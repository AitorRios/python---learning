#Cajero automático 
#falta, control de acceso, procesos.
#entrada
Cliente = {
    "Nombre": "aitor", 
    "contraseña": "123456", 
    "saldo": 0 
}

nombre = input("Introduce su nombre:")
control = input("Introduce su contraseña:")


menu = ["1", "2", "3", "4"]
print("consultar saldo - 1")
print("Ingresar dinero - 2")
print("Sacar dinero - 3")
print("Salir - 4")
while True:
    eleccion = input("selecciona uno de las opciones:")
    if eleccion not in menu:
        print("Por favor. Elije una opcion correcta con números")
    else:
        break
    



#datos internos
quinientos = 0
doscientos = 0
cien = 0
cincuanta = 0
diez = 0 
cinco = 0