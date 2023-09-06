# Pedir al usuario que ingrese las horas trabajadas y la tarifa por hora
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))

# Calcular el sueldo base
sueldo_base = horas_trabajadas * tarifa_por_hora


# Calcular el sueldo total, que incluye el sueldo base y el bono por horas extras
sueldo_total = sueldo_base

# Mostrar el sueldo total al empleado
print(f"El sueldo total del empleado es: ${sueldo_total:.2f}")
