def receta(nombre, fecha, direccion, medicamento, dosis, instrucciones, turno):
    print("----------------------------------------------------------")
    print("nombre del paciente:",nombre.center(22))
    print("fecha de nacimiento:",fecha.center(22))
    print("medicamento recetado:",medicamento.center(22))
    print("dosis del medicamento:",dosis.center(22))
    print("instrucciones de uso:",instrucciones.center(22))

    print("su proximo turno es el",turno.center(22))
    print("----------------------------------------------------------")

    print("ante cualquier consulta, estamos ubicados en",direccion)

nombre = input("ingrese su nombre completo")
fecha = input("ingrese su fecha de nacimiento")
turno = input("cuando es su proximo turno?")
direccion = input("ingrese la ubicacion de la clinica")
medicamento = input("ingrese el nombre del medicamento recetado")
dosis = input("ingrese la dosis del medicamento")
instrucciones = input("ingrese las instrucciones de uso del medicamento")

receta(nombre,fecha,direccion,medicamento,dosis,instrucciones,turno)




