
#Pedir informacion

nombre = input("Ingrese el nombre del paciente: ")
fechaNacimiento = input("Ingrese la fecha de nacimiento: ")
direccionClinica = input("Ingrese la direccion de la clinica: ")
nombreMedicamento = input("Ingrese el nombre del medicamento: ")
dosisMedicamento = input("Ingrese la dosis del medicamento: ")
instruccionesDeUso = input("Ingrese las intrucciones de uso: ")



#Imprimir informacion como receta
def recetamedica():
    print("Receta clinica")
    print("El nombre del paciente es: ",nombre)
    print("La fecha de nacimiento es:", fechaNacimiento)
    print("Ubicacion de la clinica: ",direccionClinica)
    print(f"Informacion del remedio: \n-Nombre del medicamento: {nombreMedicamento} \n-Dosis del medicamento: {dosisMedicamento} "
          f"\n-Instrucciones de uso: {instruccionesDeUso}")


recetamedica()