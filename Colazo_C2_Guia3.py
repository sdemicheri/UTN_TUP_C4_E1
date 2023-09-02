"""GUIA NUMERO 3
   COLAZO FERNANDO"""

# EJERCICIO NÚMERO 1 Y 2

#Defino la función para imprimir los datos del paciente
def imprimirdatospaciente(NOMBRE, FE_NAC):
    print("------DATOS DEL PACIENTE------")
    print("👩‍🔬 NOMBRE Y APELLIDO: ", NOMBRE)
    print("📅 FECHA DE NACIMIENTO: ", FE_NAC)

#Defino la función para imprimir los datos de la clínica
def imprimirdatosclinica(CLINICA, DIRECCION):
    print("-------------------------------")
    print("------DATOS DE LA CLINICA------")
    print("🏨 CLÍNICA: ", CLINICA)
    print("👉 DIRECCIÓN: ", DIRECCION)

#Defino la función para imprimir los datos del medicamento
def imprimirdatosdelmedicamento(MEDICAMENTO,dosis,modo_de_uso):
    print("-------------------------------")
    print("------SOBRE EL MEDICAMENTO------")
    print("📝 NOMBRE: ", MEDICAMENTO)
    print("💊 DOSIS: ", dosis)
    print("🤳 MODO DE USO: ", modo_de_uso)

#Defino la función para imprimir los datos del próximo turno
def imprimirdatosdelturno(fecha,hora,LUGAR, MED, tel):
    print("-------------------------------")
    print("------PRÓXIMO TURNO------")
    print("📅 FECHA: ", fecha)
    print("🕑 HORA: ", hora)
    print("🏠 LUGAR: ", LUGAR)
    print("🩺 MÉDICO: ", MED)
    print("📲 Teléfono: ", tel)
print("-------------------------------")


#donde ingreso los datos
print("DATOS DEL PACIENTE")
NOMBRE = input("Ingrese el nombre y apellido del paciente: ")
FE_NAC = input("Ingrese la fecha de nacimiento del paciente ")
print("DATOS DE LA CLÍNICA")
CLINICA = input("Ingrese  el nombre de la clínica")
DIRECCION = input("Ingrese la dirección de la clínica")
print("SOBRE EL MEDICAMENTO")
MEDICAMENTO = input("Ingrese el nombre del medicamento: ")
dosis = input("Ingrese la dósis del medicamento: ")
modo_de_uso = input("Indique el modo de uso del medicamento: ")
print("PRÓXIMO TURNO")
fecha = input("Ingrese la fecha del turno: ")
hora = input("Ingrese la hora del turno: ")
LUGAR = input("Ingrese el lugar del turno: ")
MED = input("Ingrese el nombre del profesional: ")
tel =input("Ingrese el número de teléfono: ")

imprimirdatospaciente(NOMBRE, FE_NAC)
imprimirdatosclinica(CLINICA, DIRECCION)
imprimirdatosdelmedicamento(MEDICAMENTO,dosis, modo_de_uso)
imprimirdatosdelturno(fecha,hora,LUGAR,MED, tel)


