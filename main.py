# Funcion para imprimir los arbitros designados para el partido
icono = '⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽'
def imprimirArbitros (a1, a2, a3, a4,) :
    print('⚽⚽⚽ARBITROS DESIGNADOS⚽⚽⚽')
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(icono)

def imprimirDatosCancha (nombre, dia) :
    print(icono)
    print('LUGAR')
    print(nombre)
    print('FECHA')
    print(dia)
    print(icono)

def datosLiga (direccion, telefono) :
    print(icono)
    print('Para consultas Comunicarse por estos medios')
    print('Email: ',direccion)
    print('Telefono: ',telefono)
    print(icono)

a1 = input('Ingrese el nombre del primer arbritro: ')
a2 = input('Ingrese el nombre del segundo arbritro: ')
a3 = input('Ingrese el nombre del tercer arbritro: ')
a4 = input('Ingrese el nombre del ultimo arbritro: ')
cancha = input('Ingrese el nombre de la cancha: ')
dia = input('Ingrese el dia: ')
direccion = input('Ingrese la direccion de correo de la cancha: ')
telefono = input('Ingrese el numero de telefono de la liga: ')

imprimirArbitros(a1, a2, a3, a4)
imprimirDatosCancha(cancha, dia)
datosLiga(direccion, telefono)