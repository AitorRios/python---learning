#Cajero automático 
#falta, control de acceso, procesos.
#entrada
Cliente = {
    "Nombre": "aitor", 
    "contraseña": "123456", 
    "saldo": 0 
}

def autentificacion ():
        while True:
            nombre = input("Introduce su nombre:")
            contraseña = input("Introduce su contraseña:")
            if nombre.lower() == Cliente["Nombre"] and contraseña == Cliente["contraseña"]:
                print("\nSesion iniciada!\n")
                return menu()
            else:
                print("Nombre o contraseña erroneos")
def menu():        
        menu = ["1", "2", "3", "4", "uno", "dos", "tres", "cuatro"]
        print("consultar saldo - 1")
        print("Ingresar dinero - 2")
        print("Sacar dinero - 3")
        print("Salir - 4")
        while True:
            eleccion = input("selecciona uno de las opciones:")
            if eleccion.lower() not in menu:
                print("Por favor. Elije una opcion correcta.\n")
            else:
                return



#datos internos
billete_500 = 0
billete_200 = 0
billete_100 = 0
billete_50 = 0
billete_10 = 0 
billete_5= 0