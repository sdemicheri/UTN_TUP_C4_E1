def registrar_consulta():
    nombre_apellido = input("Ingrese el nombre y apellido del paciente: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente (DD/MM/AAAA): ")

    medicamento = input("Ingrese el nombre del medicamento recetado: ")
    dosis = input("Ingrese la dosis del medicamento: ")
    instrucciones = input("Ingrese las instrucciones de uso del medicamento: ")

    # Mostrar la información de la consulta y la receta
    print("Información de la consulta médica:")
    print(f"Nombre del paciente: {nombre_apellido}")
    print(f"Fecha de nacimiento: {fecha_nacimiento}")
    print("Receta Médica:")
    print(f"Medicamento recetado: {medicamento}")
    print(f"Dosis: {dosis}")
    print(f"Instrucciones de uso: {instrucciones}")
registrar_consulta()
