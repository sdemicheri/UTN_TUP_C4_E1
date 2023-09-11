#defino una funcion para imprimir la direccion de la clinica
def imprimirDireccion (direccion):
    print("RECETA MEDICA")
    print(direccion)
#defino una funcion para imprimir datos del paciente
def imprimirNombreyFecha (nombre,fecha):
    print(nombre)
    print(fecha)
#defino una funcion para imprimir datos del medicamento recetado
def imprimirMedicamentoRecetado (nombreMedicamento,dosis,instrucciones):
    print(nombreMedicamento)
    print(dosis)
    print(instrucciones)

#defino una funcion para imprimir datos del siguiente turno del paciente
def ImprimirSiguienteTurno (nombre2,fecha2,hora):
    print("SIGUIENTE TURNO")
    print(nombre2)
    print(fecha2)
    print(hora)
#parte del codigo donde ingreso los datos
direccion= input("Ingrese la direccion de la clinica: ")
nombre= input("Ingrese el nombre del paciente: ")
fecha= input("Ingrese la fecha de nacimiento: ")
nombreMedicamento= input("Ingrese el nombre del medicamento: ")
dosis= input("Ingrese la dosis: ")
instrucciones= input("Ingrese las instrucciones del medicamento: ")
nombre2= input("Ingrese el nombre del paciente: ")
fecha2= input("Ingrese la fecha del siguiente turno: ")
hora= input("Ingrese la hora del turno: ")


imprimirDireccion(direccion)
imprimirNombreyFecha(nombre,fecha)
imprimirMedicamentoRecetado(nombreMedicamento,dosis,instrucciones)
ImprimirSiguienteTurno(nombre2,fecha2,hora)

