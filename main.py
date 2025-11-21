from utils import *


while True:
    x = int(input("Que opcion quieres : 1) Registro 2) Busqueda 3) Reportes 4) Modificaciones 5) Eliminar 6) Salir "))
    match x:
        case 1:
            register(int(input("Ingrese el numero de personas a hospedar: "))) 

        case 2:
            print(searchByRoom(int(input("Ingrese el numero de habitacion a buscar: "))))
        case 3:
            opcion = input("a) Ver todos los registros b) Ver habitaciones ocupadas ").lower()
            if opcion == "a":
                with open("registro.txt", "r") as f:
                    for line in f: 
                        print(line)
            else:
                occupied = getOcuppied()
                print("H1 ||H2 ||H3 ||H4 ||H5 ||H6 ||H7 ||H8 ||H9 ")
                for i in range(1, 10):
                    if i in occupied:
                        print("X || ", end="")
                    else:
                        print("O || ", end="")
                print()
                 

        case 4:
            modifyRecord(int(input("Ingrese el numero de habitacion a modificar: ")))
    
        case 5:
            habitacion = searchByRoom(int(input("Ingrese el numero de habitacion a buscar: ")))
            if habitacion:
                lines = []
                with open("registro.txt", "r") as f:
                    lines = f.readlines()
                with open("registro.txt", "w") as f:
                    for line in lines:
                        if line != habitacion:
                            f.write(line)      
                print("Registro eliminado.")
            else:
                print("Habitacion no encontrada.")
        case 6:
            print("Ingresos Totales: ", totalIncome())
            exit()
        case _:
            print("Opcion no valida")

    