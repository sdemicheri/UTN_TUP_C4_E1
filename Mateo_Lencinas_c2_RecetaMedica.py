# Receta médica - Guía n.º 3 #

def imprimir_datos(nombre,fecha_nacimiento,direccion_clinica,medicamento,medicamento_dosis,medicamento_instrucciones,date,time, doctor):
    print(f"""
------------------------------------------------------------------------------------------------------------------------
    
    Nombre y Apellido: {nombre}
    Fecha de nacimiento: {fecha_nacimiento}
    Direccion de la clinica medica: {direccion_clinica}
    
    Detalles del medicamento 
    Medicamento: {medicamento}
    Dosis: {medicamento_dosis}
    Instrucciones de uso: {medicamento_instrucciones}
    
    __________________________________________________________________
    
    Siguente turno
    Nombre y Apellido: {nombre}
    Fecha: {date}
    Hora: {time}
    Nombre y Apellido doctor/a: {doctor} 
    
------------------------------------------------------------------------------------------------------------------------
    """)

nombre = input("Ingresar el nombre completo del paciente: ")
fecha_nacimiento = input("Ingresar la fecha de nacimiento del paciente: ")
direccion_clinica = input("Ingresar la direccion de la clinica medica: ")
print("\nDetalles del medicamento:")
medicamento = input("Ingresar nombre del medicamento: ")
medicamento_dosis = input("Ingresar la dosis: ")
medicamento_intrucciones = input("Ingresar las instrucciones de uso: ")
print("\nSiguiente turno:")
date = input("Ingrese fecha del turno: ")
time = input("Ingrese hora del turno: ")
doctor = input("Ingrese el nombre completo del doctor/a: ")

imprimir_datos(nombre,fecha_nacimiento,direccion_clinica,medicamento,medicamento_dosis,medicamento_intrucciones,date,time,doctor)
