# defino una funcion para imprimir los datos de los arbitros
def imprimirArbitros(a1, a2, a3, a4):
    print("⚽⚽ARBITROS DESIGNADOS⚽⚽")
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print("⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽")

def filaAsteriscos():
    print("***************************************")
    print("⚽"*21)
    print("***************************************")

# defino una funcion para imprimir los datos de la cancha
def imprimirDatosCancha(nombre, dia):
    print("LUGAR")
    print(nombre)
    print("FECHA")
    print(dia)


# parte del codigo donde ingreso los datos
a1 = input('Ingrese el nombre del arbitro a1: ')
a2 = input('Ingrese el nombre del arbitro a2: ')
a3 = input('Ingrese el nombre del arbitro a3: ')
a4 = input('Ingrese el nombre del arbitro a4: ')
cancha = input('Ingrese el nombre de la cancha: ')
dia = input('Ingrese el dia: ')
filaAsteriscos()
imprimirArbitros(a1, a2, a3, a4)
filaAsteriscos()
imprimirDatosCancha(cancha, dia)
filaAsteriscos()
