# salida:
#   sistema de nóminas
# entrada:
#   datos del trabajador
#   horas trabajadas
#   costo por hora

# Defino funcion para imprimir los datos del trabajador
def datosTrabajador(nombre, mesCobro, yCobro):
    print("👔-NOMBRE DEL EMPLADO:", nombre)
    print("📅-MES DE COBRO:", mesCobro)
    print("📆-AÑO DE COBRO:", yCobro)

# Defino funcion para imprimir los datos de la paga del trabajador
def pagaTrabajador(hsT, costoHs, pago):
    print("⌚-HORAS TRABAJADAS:", hsT)
    print("💲-COSTO DE LAS HORAS:", costoHs)
    print("💵-PAGO:", pago)

# Defino funcion para imprimir separador
def separador():
    print("-=⭕=-=⭕=-=⭕=-=⭕=-=⭕=-=⭕=-")

nombre = input("Ingrese el nombre del emplado:")
mesCobro = input("Ingrese el mes de cobro:")
yCobro = input("Ingrese el año de cobro:")
hsT = int(input("Ingrese las horas trabajadas:"))
costoHs = int(input("Ingrese el costo de las horas:"))
pago = hsT*costoHs

separador()
datosTrabajador(nombre, mesCobro, yCobro)
separador()
pagaTrabajador(hsT, costoHs, pago)
separador()