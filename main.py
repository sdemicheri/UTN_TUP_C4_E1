# salida:
#   receta impresa
# entrada:
#   nombre completo del paciente
#   fecha de nacimiento del paciente
#   direccion de la clinica
#   detalles del medicamento(nombre, dosis e instrucciones)


# defino funcion para imprimir los datos del paciente
def datosPaciente(nombre,fecha):
    print("├--DATOS DEL PACIENTE")
    print("├", nombre)
    print("├", fecha)

# defino funcion para imprimir la dirección de la clinica
def direcClinica(direccion):
    print("├--DIRECCIÓN DE LA CLINICA")
    print("├", direccion)

# defino funcion para imprimir los detalles del medicamento
def detallesMedicamento(medicamento,dosis,instruc):
    print("├--DETALLES DEL MEDICAMENTO")
    print("├", medicamento)
    print("├", dosis)
    print("├", instruc)

# funcion para imprimir separador
def separador():
    print("---------------------")

nombre = input("Ingrese el nombre completo del paciente:")
fecha = input("Ingrese la fecha de nacimiento del paciente:")
direccion = input("Ingrese la direccion de la clinica:")
medicamento = input("Ingrese el nombre del medicamento:")
dosis = input("Ingrese la dosis del medicamento:")
instruc = input("Ingrese las instrucciones del medicamento:")

separador()
datosPaciente(nombre, fecha)
separador()
direcClinica(direccion)
separador()
detallesMedicamento(medicamento,dosis,instruc)
separador()