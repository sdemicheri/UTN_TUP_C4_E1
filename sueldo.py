# Definir función para calcular y mostrar el sueldo del empleado.
def sueldoEmpleados(nombreEmpleado, sueldo, moneda):
    print()  # Esto imprimirá una línea en blanco en la consola.
    print("¡Sueldo Empleado!")
    print("Sueldo a nombre de:", nombreEmpleado)
    print("El sueldo es $", sueldo, moneda)

# Pedir al usuario que ingrese su nombre y la moneda.
nombreEmpleado = input("Ingrese su nombre: ")
moneda = input("Ingrese nombre de la moneda: ")

# Pedir al usuario que ingrese el número de horas trabajadas y el costo por hora.
horasTrabajadas = float(input("Ingrese número de horas trabajadas: "))
costoPorHora = float(input("Ingrese el costo por hora: "))

# Calcular el sueldo multiplicando las horas trabajadas por el costo por hora.
sueldo = horasTrabajadas * costoPorHora

# Llamar a la función para mostrar el sueldo del empleado.
sueldoEmpleados(nombreEmpleado, sueldo, moneda)
