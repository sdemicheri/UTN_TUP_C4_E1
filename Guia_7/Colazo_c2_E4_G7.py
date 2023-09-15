"""Colazo Fernando
   Guía 7
   Ejercicio 3

   En un circuito electrico hay 3 interruptores los cuales pueden
   estar en el estado cerrad(1), abierto (0). Para que un equipo funcione se
   requiere que al menos dos esten cerrados. Si los datos son los estados de los interruptores
   determine si el equipo funcionará"""
try:
    print("ESTADO DE LOS INTERRUPTORES: \n1 = cerrado\n0 = abierto")
    i1 = int(input("Ingrese el estado del interruptor 1: "))
    i2 = int(input("Ingrese el estado del interruptor 2: "))
    i3 = int(input("Ingrese el estado del interruptor 3: "))
    estado_equipo = i1 + i2 + i3
    if i1 < 0 or i2 < 0 or i3 < 0:
        print("Ingrese un valor correcto: \n-Un 0 si el interruptor está abierto\n-Un 1 si el interruptor está cerrado")
    elif i1 > 1 or i2 > 1 or i3 > 1:
        print("Ingrese un valor correcto: \n-Un 0 si el interruptor está abierto\n-Un 1 si el interruptor está cerrado")
    elif estado_equipo >= 2 and estado_equipo <= 3:
        print("El equipo está funcionando")
    elif estado_equipo < 2:
        print("El equipo no está funcionando")
except ValueError:
    print("Ingrese un valor númerico positivo entre 0 y 1")