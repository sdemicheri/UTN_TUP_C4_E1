def recetaMedica (nombre ,fechaNac ,direccion1 ,nomMedicam ,dosis ,instruccion):
    print("           🗓️RECETA MÉDICA🗓️              ")

    print(f"Nombre: {nombre}")
    print(f"Fecha de nacimiento: {fechaNac}")
    print(f"Direccion de la clínica: {direccion1}")
    print(f"Nombre medicamemto: {nomMedicam}")
    print(f"Dosis: {dosis}")
    print(f"Instrucciones: {instruccion}")

    print("---------------------------------------------")

def proxTurno (fecha,hora,direccion2,medico):
    print("           🗓️PRÓXIMO TURNO🗓️              ")

    print(f"Fecha: {fecha}")
    print(f"Horario: {hora}")
    print(f"Dirección: {direccion2}")
    print(f"Médico: {medico}")


nombre = input("Ingrese el nombre completo del paciente: ")
fechaNac = input("Fecha de nacimiento: ")
direccion1 = input("Dirección de la clínica: ")
nomMedicam = input("Nombre del medicamento: ")
dosis = input("Dosis: ")
instruccion = input("Instrucciones: ")
print("---------------------------------------------")
fecha = input("Fecha próximo turno: ")
hora = input("Horario: ")
direccion2 = input("Dirección: ")
medico = input("Medico: ")
print("---------------------------------------------")


recetaMedica(nombre,fechaNac,direccion1,nomMedicam,dosis,instruccion)
proxTurno(fecha,hora,direccion2,medico)
print("⚕️⚕️⚕️⚕️⚕️⚕️⚕️⚕️⚕️⚕️⚕️⚕️⚕️⚕️⚕️⚕️⚕️⚕️⚕️⚕️⚕️⚕️")