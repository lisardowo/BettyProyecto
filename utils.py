
def register(Personas)   :   
    
    TotalApagar = 0
    NumHab = int(input("Ingrese el numero de la habitacion: "))
    
    f = open("registro.txt", "r")
    lineas = f.readlines()
    f.close()

    for i in range(len(lineas)):

        with open("registro.txt", "r") as f:
            for line in f: 
                if f"Numero de Habitacion: {NumHab}" in line:
                    print("Habitacion ya ocupada.")
                    f.close()
                    return 1

    NumDias = int(input("Ingrese el numero de dias a hospedar: "))
    if Personas == 1:
        TotalApagar = 1000
    elif Personas == 2:
        TotalApagar = 1500
        
    else:
        for i in range(Personas):
            TotalApagar += 500
    
    
    Nombre = input("Ingrese el nombre: ")
    CdOrigen = input("Ingrese la Ciudad de origen: ")
      
    FormaDepago = input("Ingrese la forma de pago:(Efectivo o Tarjeata) ")

    f = open("registro.txt", "a")  
    f.write(f"Numero de Habitacion: {NumHab}, Numero de Dias: {NumDias}, Numero de Personas: {Personas}, Total a Pagar: {TotalApagar * NumDias}, Forma de Pago: {FormaDepago}\n")
    f.close()
    print(f"Registro exitoso, tu total a pagar es: {TotalApagar * NumDias}.")
    return 0

def searchByRoom(NumHab):
    with open("registro.txt", "r") as f:
        for line in f: 
            if f"Numero de Habitacion: {NumHab}" in line:
                f.close()
                return line
    print("Habitacion no encontrada.")
    return 2

def getOcuppied():
    occupied: list[int] = []
    with open("registro.txt", "r") as f:
        for line in f: 
            parts = line.split(",")
            for part in parts:
                if "Numero de Habitacion" in part:
                    num_hab = int(part.split(":")[1].strip())
                    occupied.append(num_hab)
    return occupied

def modifyRecord(NumHab):
    with open("registro.txt", "r+") as f:
        for line in f: 
            if f"Numero de Habitacion: {NumHab}" in line:
                parts = line.split(",")
                NumDias = int(parts[1].split(":")[1].strip())
                Personas = int(parts[2].split(":")[1].strip())
                TotalApagar = int(parts[3].split(":")[1].strip())
                FormaDepago = parts[4].split(":")[1].strip()
                if Personas == 1:
                    TotalApagar = 1000
                elif Personas == 2:
                    TotalApagar = 1500
                else:
                    for i in range(Personas):
                        TotalApagar = 0
                        TotalApagar += 500
                print("Ingrese los nuevos datos.")
                DiasExtra = int(input("Ingrese el numero de dias extra de su estancia: "))
                mods = f"Numero de Habitacion: {NumHab}, Numero de Dias: {NumDias + DiasExtra}, Numero de Personas: {Personas}, Total a Pagar: {TotalApagar * (NumDias + DiasExtra)}, Forma de Pago: {FormaDepago}\n"
                f.seek(0)
                lines = f.readlines()
                f.seek(0)
                f.truncate()
                for l in lines:
                    if l == line:
                        f.write(mods)
                    else:
                        f.write(l)
                print("Registro modificado exitosamente.")
            return 0
def totalIncome():
    total = 0
    with open("registro.txt", "r") as f:
        for line in f: 
            parts = line.split(",")
            for part in parts:
                if "Total a Pagar" in part:
                    amount = int(part.split(":")[1].strip())
                    total += amount
    return total