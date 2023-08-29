def main():
    nombre = input("Introduzca el nombre completo del paciente: ")
    fechaNac = input("Introduzca la fecha de nacimiento del paciente: ")
    direccion = input("Introduzca la dirección de la Clínica Médica: ")
    detalleMed = input("Introduzca los detalles del medicamento (nombre, dosis e instrucciones de uso): ")
    crearTicket(nombre, fechaNac, direccion, detalleMed)


def crearTicket(nombre, fecha, dir, detalles):
    print(f"""
    Nombre del paciente: {nombre}
    Fecha de nacimineto del paciente: {fecha}
    Dirección de la Clínica Médica: {dir}
    Detalles del medicamento recetado: {detalles}
    """)


main()