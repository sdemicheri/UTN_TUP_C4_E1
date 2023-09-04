# Esta función recibe los datos generales y los imprime por "print()" con un formato prediseñado.
def imprimirReceta (direccion, nombrePaciente, fechaNacimiento, nombreMedicamento, dosisMedicamento, instrucciones, fecha, hora) :
    separador = "────────────────────────────────────────"

    print(separador)
    print("🏥 Direccion:", direccion)
    print(separador)
    print("🙍‍♀️ Datos del paciente 🙍‍♂️")
    print("Nombre: ", nombrePaciente)
    print("Fecha de nacimiento: ", fechaNacimiento)
    print(separador)
    print("💊 Medicamento: ", nombreMedicamento)
    print("dosis: ", dosisMedicamento)
    print("👇 Instrucciones de medicamente 👇")
    print("")
    print(instrucciones)
    print(separador)
    # en caso de que las variables tengan un valor diferente a "None" se ejecuta el condicional
    if (fecha and hora) : 
        print("Proximo turno:")
        print("Fecha: ", fecha)
        print("Hora: ", hora)
        print(separador)

# Solicitamos la informacion del paciente, direccion de la clinica y datos e instrucciones del medicamento 
direccion = input("Ingrese la direccion de la clinica: ")
print("")
print("A continuacion ingrese los datos del paciente")
print("")
nombrePaciente = input("Nombre: ")
fechaNacimiento = input("Fecha de nacimiento: ")
print("")
print("Por ultimo ingrese los datos del medicamento")
print("")
nombreMedicamento = input("Nombre: ")
dosisMedicamento = input("Dosis recetada: ")
instrucciones = input("Instrucciones de uso: ")

# Declaramos variables nulas de fecha y hora 
fecha = None
hora= None
# preguntamos si se quiere agregar un turno proximo en la receta medica
preguntaTurno = input("¿Quieres agregar el proximo turno del paciente a la receta? Si/No ")

# en caso de que la variable contenga el valor de "Si" se ejecuta el condicional
if (preguntaTurno.lower() == "si") :
    # asignamos los valores correspondientes a las variables anteriormente creadas
    fecha = input("Ingrese la fecha del proximo turno: ")
    hora = input("Ingrese la hora del proximo turno: ")


imprimirReceta(direccion, nombrePaciente, fechaNacimiento, nombreMedicamento, dosisMedicamento, instrucciones, fecha, hora)
