#Defino una función para imprimir los datos de los arbitros
def imprimirArbitros(a1, a2, a3, a4) :
    print("⚽⚽Arbitros Designados⚽⚽")
    print("⚽", a1, "⚽", a2, "⚽", a3, "⚽", a4, "⚽")

#Defino una función para imprimir los datos de la cancha, dia y hora
def imprimirDatosCancha(nombreLugar, dia, hora) :
    print("⚽⚽LUGAR⚽,⚽FECHA📅⚽Y⚽HORA⌚⚽")
    print("⚽", nombreLugar, "⚽", dia, "⚽", hora, "⚽")

#Defino una función para imprimir los datos de dirección y telefono
def imprimirDatosLiga(direccionCorreo, telefono) :
    print("⚽⚽DIRECCIÓN CORREO⚽Y⚽TELEFONO📞⚽")
    print("⚽", direccionCorreo, "⚽", telefono, "⚽")

#Parte del codigo donde ingreso los datos
a1 = input("Ingrese nombre del arbitro a1:")
a2 = input("Ingrese nombre del arbitro a2: ")
a3 = input("Ingrese nombre del arbitro a3: ")
a4 = input("Ingrese nombre del arbitro a4: ")
nombreLugar = input("Ingrese el nombre de la cancha: ")
dia = input("Ingrese el dia: ")
hora = input("Ingrese el horario: ")
direccionCorreo = input("Ingrese la direccion del Correo: ")
telefono = input("Ingrese el telefono: ")

#Separador
print("")
imprimirArbitros(a1, a2, a3, a4)
imprimirDatosCancha(nombreLugar, dia, hora)
imprimirDatosLiga(direccionCorreo, telefono)
