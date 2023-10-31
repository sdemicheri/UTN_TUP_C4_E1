##TICKET DE FUTBOL##
#Sergio, es el encargado de la liga de fútbol en tu localidad, él es quien lleva los registros del fixture, de los partidos jugados, las tablas de posiciones, entre otras cosas. Una de sus funciones es asegurarse que los técnicos de los equipos estén bien informados. Para ellos cuenta con los detalles esenciales del encuentro: la cancha donde se llevará a cabo, la fecha y hora del juego, así como los nombres de los cuatro árbitros que supervisarán el partido. Con la responsabilidad de entregar la información de manera eficiente, decide crear tickets que contengan todos estos datos cruciales. Estos tickets serán entregados a cada uno de los técnicos de los equipos participantes. Para llevar a cabo esta tarea, necesita diseñar los tickets impresos y asegurarse de que los nombres de los árbitros estén destacados, junto con la dirección exacta de la cancha, la fecha en que se llevará a cabo el partido y el horario preciso en el que comenzará. La información debe visualizarse de manera clara y comprensible para los técnicos, asegurando así que estén preparados para el evento deportivo.

#DATOS DE ENTRADA#
#Nombres de los arbitros - direccion de la cancha - fecha del partido - horario preciso del partido

#Arbitros
arbitro1 = str(input("nombre del 1° arbitro: "))
arbitro2 = str(input("nombre del 2° arbitro: "))
arbitro3 = str(input("nombre del 3° arbitro: "))
arbitro4 = str(input("nombre del 4° arbitro: "))

#Direccion de la cancha
cancha1 = str(input("Cancha donde estará el 1° arbitro"))
cancha2 = str(input("Cancha donde estará el 2° arbitro"))
cancha3 = str(input("Cancha donde estará el 3° arbitro"))
cancha4 = str(input("Cancha donde estará el 4° arbitro"))

#Fecha del partido
fecha_partido1 = str(input("Fecha del partido donde estará el 1° arbitro: "))
fecha_partido2 = str(input("Fecha del partido donde estará el 2° arbitro: "))
fecha_partido3 = str(input("Fecha del partido donde estará el 3° arbitro: "))
fecha_partido4 = str(input("Fecha del partido donde estará el 4° arbitro: "))

#Horarios precisos de los partidos
horario_partido1 = str(input("horario del partido donde estará el 1° arbitro: "))
horario_partido2 = str(input("horario del partido donde estará el 2° arbitro: "))
horario_partido3 = str(input("horario del partido donde estará el 3° arbitro: "))
horario_partido4 = str(input("horario del partido donde estará el 4° arbitro: "))

#DATOS DE SALIDA#
#la cancha donde se llevará a cabo - la fecha y hora del juego - los nombres de los cuatro árbitros.
print(f"ARBITRO: {arbitro1} \nCANCHA: {cancha1} \nFECHA: {fecha_partido1} \nHORARIO: {horario_partido1} \n\nARBITRO: {arbitro2} \nCANCHA: {cancha2} \nFECHA: {fecha_partido2} \nHORARIO: {horario_partido2} \n\nARBITRO: {arbitro3} \nCANCHA: {cancha3} \nFECHA: {fecha_partido3} \nHORARIO: {horario_partido3} \n\nARBITRO: {arbitro4} \nCANCHA: {cancha4} \nFECHA: {fecha_partido4} \nHORARIO: {horario_partido4}")