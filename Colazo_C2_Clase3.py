"""EJERCICIO DE LA CALSE 3
   COLAZO FERNANDO"""

#defino una función para imprimir los datos del empleado
def imprimirdatosempleado(NOM, HS, costo, MES, PAGO, AÑO):
    print("-" * 40)
    print("NOMBRE Y APELLIDO: ", NOM)
    print("-" * 40)
    print("MES |   AÑO   | HORAS TRABAJADAS ")
    print(MES, " | ", AÑO, "  |     ", HS)
    print("-" * 40)
    print("COSTO POR HORA | REMUNERACIÓN")
    print(" " * 4, costo, "     |  ", " $", PAGO, )
    print("-" * 40)


NOM = input("Ingrese su nombre y apellido: ")
MES = input("Ingrese el mes en números correspondiente al pago: ")
AÑO = input("Ingrese el año correspondiente al pago: ")
HS = float(input("Ingrese la cantidad de horas totales que trabajo en el mes: "))
costo = float(input("Ingrese cuanto gana por hora trabajada: "))
PAGO = (HS*costo)

imprimirdatosempleado(NOM, HS, costo, MES, PAGO, AÑO)