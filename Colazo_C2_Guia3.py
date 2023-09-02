#Defino la función para imprimir los datos del paciente
def imprimirdatospaciente(NOMBRE, FE_NAC):
    print("------DATOS DEL PACIENTE------")
    print("NOMBRE Y APELLIDO: ", NOMBRE)
    print("FECHA DE NACIMIENTO: ", FE_NAC)

#Defino la función para imprimir los datos de la clínica
def imprimirdatosclinica(CLINICA, DIRECCION):
    print("-------------------------------")
    print("------DATOS DE LA CLINICA------")
    print("CLÍNICA: ", CLINICA)
    print("DIRECCIÓN: ", DIRECCION)

#Defino la función para imprimir los datos deL medicamento
def imprimirdatosdelmedicamento(MEDICAMENTO,dosis,modo_de_uso):
    print("-------------------------------")
    print("------SOBRE EL MEDICAMENTO------")
    print("NOMBRE: ", MEDICAMENTO)
    print("DOSIS: ", dosis)
    print("MODO DE USO: ", modo_de_uso)


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

imprimirdatospaciente(NOMBRE, FE_NAC)
imprimirdatosclinica(CLINICA, DIRECCION)
imprimirdatosdelmedicamento(MEDICAMENTO,dosis, modo_de_uso)