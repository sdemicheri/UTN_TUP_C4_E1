print("⚽ Información necesaria para la creación del ticket del partido ⚽")
a1 = input("Ingrese el nombre del árbitro titular:")
a2 = input("Ingrese el nombre del árbitro suplente:")
a3 = input("Ingrese el nombre del juez de linea 1:")
a4 = input("Ingrese el nombre del juez de linea 2:")
cancha = input("Ingrese el nombre del estadio en donde se jugará el partido:")
fecha = input("Ingrese fecha en que se jugará el partido:")
hora = input("Ingrese hora en que arrancará el partido:")

print("------------------------------------------------------------------------------")
print("⚽⚽⚽⚽⚽⚽TICKET DEL PARTIDO⚽⚽⚽⚽⚽⚽")
print("El partido estará arbitrado por los siguientes jueces:")
print("🏃‍♂️Árbitro titular:",a1,)
print("🏃‍♂️Árbitro suplente:",a2,)
print("🚩Juez de línea 1:",a3,)
print("🚩Juez de línea 2:",a4,)
print("El partido se realizara a las:",hora,"en el estadio",cancha,"el dia",fecha,)
print("-------------------------------------------------------------------------------")

