# Defino una función para imprimir los datos del Paciente.
def imprimirDatosPaciente(nombrePaciente, nacimientoPaciente):
    print("🧑🏼Datos  Del Paciente👨🏼‍🦱")
    print("Nombre: ", nombrePaciente)
    print("Fecha de nacimiento: ", nacimientoPaciente)
    print("-\t-\t-\t-\t-\t-\t-")

# Defino una función para imprimir los datos de la clinica medica.
def imprimirDatosClinica(direccionClinica):
    print("🏥Datos De La Clinica🏥")
    print("direccion: ", direccionClinica)
    print("-\t-\t-\t-\t-\t-\t-")

# Defino una función para imprimir los datos de dirección y telefono.
def imprimirDetallesMedicamento(nombreMedicamento, dosisMedicamento, instruccionMedicamentoUso):
    print("🩺Detalles Del Medicamento💊")
    print("Nombre: ", nombreMedicamento)
    print("Número de dosis: ", dosisMedicamento)
    print("Instruccion de uso: ", instruccionMedicamentoUso)

# Parte del codigo donde ingreso los datos.
nombrePaciente = input("Ingrese nombre completo del paciente: ")
nacimientoPaciente = input("Ingrese fecha de nacimiento del paciente: ")
direccionClinica = input("Ingrese direccion de la clinica medica: ")
nombreMedicamento = input("Ingrese el nombre del medicamento: ")
dosisMedicamento = int(input("Ingrese el numero de dosis del medicamento: "))
instruccionMedicamentoUso = input("Ingrese las instrucciones de uso: ")

imprimirDatosPaciente(nombrePaciente, nacimientoPaciente)
imprimirDatosClinica(direccionClinica)
imprimirDetallesMedicamento(nombreMedicamento, dosisMedicamento, instruccionMedicamentoUso)
