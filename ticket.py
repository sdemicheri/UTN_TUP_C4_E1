def arbitros(arbitro1,arbitro2,arbitro3,arbitro4):
    print("----------------------------------------------------------")
    print("arbitros a supervisar el partido:")
    print(arbitro1)
    print(arbitro2)
    print(arbitro3)
    print(arbitro4)

def lugar(cancha):
    print("informacion del encuentro:")
    print("lugar:", cancha)

def fechayhora(fecha,hora):
    print("fecha y hora:", fecha, "a las", hora)


def contacto(telefono,correo):
    print("datos de contacto:")
    print("telefono:",telefono)
    print("correo electronico:",correo)
    print("----------------------------------------------------------")

arbitro1 = input("ingrese el nombre del primer arbitro")
arbitro2 = input("ingrese el nombre del segundo arbitro")
arbitro3 = input("ingrese el nombre del tercer arbitro")
arbitro4 = input("ingrese el nombre del cuarto arbitro")
cancha = input("ingrese el nombre del cancha")
fecha = input("ingrese la fecha")
hora = input("ingrese la hora")
telefono = input("ingrese el numero telefonico de la guia")
correo = input("ingrese el correo electronico de la liga")

arbitros(arbitro1,arbitro2,arbitro3,arbitro4)
lugar(cancha)
fechayhora(fecha,hora)
contacto(telefono,correo)



