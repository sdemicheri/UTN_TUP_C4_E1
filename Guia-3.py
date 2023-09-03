# Defino una función para imprimir los datos del Paciente.
def imprimirDatosPaciente(nombrePaciente, nacimientoPaciente):
    print("🧑🏼Datos Del Paciente👨🏼‍🦱")
    print("Nombre:", nombrePaciente)
    print("Fecha de nacimiento:", nacimientoPaciente)
    print("-\t-\t-\t-\t-\t-\t-")

# Defino una función para imprimir los datos de la clinica medica.
def imprimirDatosClinica(direccionClinica):
    print("🏥Datos De La Clinica🏥")
    print("direccion:", direccionClinica)
    print("-\t-\t-\t-\t-\t-\t-")

# Defino una función para imprimir los detalles medicos.
def imprimirDetallesMedicamento(nombreMedicamento, dosisMedicamento, instruccionMedicamentoUso):
    print("🩺Detalles Del Medicamento💊")
    print("Nombre:", nombreMedicamento)
    print("Número de dosis:", dosisMedicamento)
    print("Instruccion de uso:", instruccionMedicamentoUso)
    print("-\t-\t-\t-\t-\t-\t-")

# Defino una funcion para imprimir la fecha del proximo turno.
def imprimirProximoTurno(proximoTurno):
    print("📅Proximo Turno📅")
    print("El proximo turno es:", proximoTurno)

# Parte del codigo donde ingreso los datos.
nombrePaciente = input("Ingrese nombre completo del paciente: ")
nacimientoPaciente = input("Ingrese fecha de nacimiento del paciente: ")
direccionClinica = input("Ingrese direccion de la clinica medica: ")
nombreMedicamento = input("Ingrese nombre del medicamento: ")
dosisMedicamento = int(input("Ingrese número de dosis del medicamento (número): "))
instruccionMedicamentoUso = input("Ingrese las instrucciones de uso: ")
proximoTurno = input("Ingrese fecha del proximo turno: ")

# Salida.
imprimirDatosPaciente(nombrePaciente, nacimientoPaciente)
imprimirDatosClinica(direccionClinica)
imprimirDetallesMedicamento(nombreMedicamento, dosisMedicamento, instruccionMedicamentoUso)
imprimirProximoTurno(proximoTurno)
