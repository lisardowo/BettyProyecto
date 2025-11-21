
opcion = int(input("1) Registro 2) Busqueda 3) Reportes 4) Modificaciones 5) Eliminar 6) Salir "))
while opcion != 6:

	opcion = int(input("1) Registro 2) Busqueda 3) Reportes 4) Modificaciones 5) Eliminar 6) Salir "))

	match opcion:
		case 1:  # Registro
			ocupada = False
			huespedes = int(input("huespedes: "))
			TotalApagar = 0
			NumHab = int(input("Numero de la habitacion: "))
            
			f = open("registro.txt", "r")
			for line in f:
				if f"Numero de Habitacion: {NumHab}" in line:
					ocupada = True
					break
			f.close()
			if ocupada:
				print("Habitacion ya ocupada.")
				continue

			NumDias = int(input("Ingrese el numero de dias a hospedar: "))

			if huespedes == 1:
				TotalApagar += 1000
			elif huespedes == 2:
				TotalApagar += 1500
			else:
				for i in range(huespedes):
					TotalApagar += 500

			Nombre = input("Ingrese el nombre: ")
			CdOrigen = input("Ingrese la Ciudad de origen: ")
			FormaDepago = input("Ingrese la forma de pago:(Efectivo o Tarjeta) ")

			f = open("registro.txt", "a")
			f.write(
				f"Numero de Habitacion: {NumHab}, Numero de Dias: {NumDias}, Numero de huespedes: {huespedes}, Total a Pagar: {TotalApagar * NumDias}, Forma de Pago: {FormaDepago}\n"
			)
			f.close()
			print(f"Registro exitoso, tu total a pagar es: {TotalApagar * NumDias}.")

		case 2:  # Busqueda
			
			NumHab = int(input("Ingrese el numero de habitacion a buscar: "))
			encontrado = None
			f = open("registro.txt", "r")
			for line in f:
				if f"Numero de Habitacion: {NumHab}" in line:
					encontrado = line
					break
			f.close()
			if encontrado:
				print(encontrado.rstrip())
			else:
				print("Habitacion no encontrada.")

		case 3:  # Reportes
			opcion = input("a) Ver todos los registros b) Ver habitaciones ocupadas ").lower()
			if opcion == "a":
				f = open("registro.txt", "r")
				for line in f:
					print(line.rstrip())
				f.close()
			else:
				occupied: list[int] = []
				f = open("registro.txt", "r")
				for line in f:
					parts = line.split(",")
					for part in parts:
						if "Numero de Habitacion" in part:
							
								num_hab = int(part.split(":")[1].strip())
								occupied.append(num_hab)
							
				f.close()
				print("H1 - H2 - H3 -H4 -H5 -H6 -H7 -H8 -H9 ")
				for i in range(len(occupied)):
					if i in occupied:
						print("X || ", end="")
					else:
						print("O || ", end="")
				print()

		case 4:  # Modificaciones
			
			NumHab = int(input("Ingrese el numero de habitacion a modificar: "))
			# Leer todo y reescribir modificado
			f = open("registro.txt", "r")
			lines = f.readlines()
			f.close()
			nuevo_contenido = []
			modificado = False
			for line in lines:
				if f"Numero de Habitacion: {NumHab}" in line and not modificado:
					parts = line.split(",")
					try:
						NumDias = int(parts[1].split(":")[1].strip())
						huespedes = int(parts[2].split(":")[1].strip())
						TotalApagar = int(parts[3].split(":")[1].strip())
						FormaDepago = parts[4].split(":")[1].strip()
					except (ValueError, IndexError):
						nuevo_contenido.append(line)
						continue
					print("Ingrese los nuevos datos.")
					try:
						DiasExtra = int(input("Ingrese el numero de dias extra de su estancia: "))
					except ValueError:
						print("Dias extra invalidos, se cancela modificacion.")
						nuevo_contenido.append(line)
						continue
					# Recalcular total proporcional
					if NumDias > 0:
						tarifa_diaria = TotalApagar // NumDias
						nuevo_total = tarifa_diaria * (NumDias + DiasExtra)
					else:
						nuevo_total = TotalApagar
					mods = f"Numero de Habitacion: {NumHab}, Numero de Dias: {NumDias + DiasExtra}, Numero de huespedes: {huespedes}, Total a Pagar: {nuevo_total}, Forma de Pago: {FormaDepago}\n"
					nuevo_contenido.append(mods)
					modificado = True
					print("Registro modificado exitosamente.")
				else:
					nuevo_contenido.append(line)
			f = open("registro.txt", "w")
			for l in nuevo_contenido:
				f.write(l)
			f.close()

		case 5:  # Eliminar
			encontrado = None
			NumHab = int(input("Ingrese el numero de habitacion a buscar: "))
			f = open("registro.txt", "r")
			texto = f.readlines()
			f.close()
			for linea in texto:
				if f"Numero de Habitacion: {NumHab}" in linea:
					encontrado = linea
					break
			if encontrado:
				f = open("registro.txt", "w")
				for linea in texto:
					if linea != encontrado:
						f.write(linea)
				f.close()
				print("Registro eliminado.")
			else:
				print("Habitacion no encontrada.")

		case 6:  # Salir + Ingresos Totales
			total = 0
			f = open("registro.txt", "r")
			for line in f:
				parts = line.split(",")
				for part in parts:
					if "Total a Pagar" in part:
							amount = int(part.split(":")[1].strip())
							total += amount
						
			f.close()
			print("Ingresos Totales: ", total)
			print("Saliendo...")
			break

