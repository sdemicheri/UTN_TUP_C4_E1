#Recete medica.
#Datos de entrada: -Nombre completo. -Fecha de nacimiento. -direccion de la clinica medica. -Detalles del medicamento(nombre, dosis e instrucciones de uso).
#Proceso: El médico al terminar de analizar al paciente y saber que enfermedad o sintomas tiene deberá de darle una receta el cual será cargada a la computadora

try:
    imprimir=0
    print("-------------------DATOS-------------------------")
    Nombre_paciente=str(input("NOMBRE DEL PACIENTE\n"))
    Nacimiento=str(input("FECHA DE NACIMIENTO DEL PACIENTE (separe por '-')\n"))
    Direccion_clinica=str(input("DIRECCIÓN DE LA CLINICA MEDICA\n"))
    Detalles=str(input("DETALLES DEL MEDICAMENTO (nombre, dosis e instrucciones)\n"))
    print("--------------------------------------------")

    print("--------------------------------------------")
    imprimir=int(input("¿Imprimir reseta medica? \n1=Si \nCualquier otro numero=No\n"))
    print("--------------------------------------------")
    if imprimir==1:
        print("-------------------RECETA-------------------------")
        print(f"Nombre del paciente: {Nombre_paciente} \nFecha de nacimiento: {Nacimiento} \nDireccion de la clinica: {Direccion_clinica} \nDetalle del medicamento: {Detalles}")
        print("--------------------------------------------")

except ValueError:
    print("Ingrese un valor correcto porfavor")
