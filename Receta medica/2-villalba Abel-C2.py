try:
    imprimir=0
    print("-------------------DATOS-------------------------")
    Nombre_paciente=str(input("NOMBRE DEL PACIENTE\n"))
    Nacimiento=str(input("FECHA DE NACIMIENTO DEL PACIENTE (separe por '-')\n"))
    Direccion_clinica=str(input("DIRECCIÓN DE LA CLINICA MEDICA\n"))
    Detalles=str(input("DETALLES DEL MEDICAMENTO (nombre, dosis e instrucciones)\n"))
    prox_turno=str(input("FECHA PARA EL PROXIMO TURNO\n"))
    print("--------------------------------------------")

    print("--------------------------------------------")
    imprimir=int(input("¿Imprimir reseta medica? \n1=Si \nCualquier otro numero=No\n"))
    print("--------------------------------------------")
    if imprimir==1:
        print("-------------------RECETA-------------------------")
        print(f"Nombre del paciente: {Nombre_paciente} \nFecha de nacimiento: {Nacimiento} \nDireccion de la clinica: {Direccion_clinica} \nDetalle del medicamento: {Detalles} \nFecha para el proximo turno:  ")
        print("--------------------------------------------")
    

except ValueError:
    print("Ingrese un valor correcto porfavor")