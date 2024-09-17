# Solicitar datos del empleado
nombre = input("Ingrese el nombre del empleado: ")
salario_por_hora = float(input("Ingrese el salario por hora: "))
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))

# Calcular paga
paga = salario_por_hora * horas_trabajadas

# Imprimir resultado
print("Nombre del empleado:", nombre)
print("Salario por hora:", salario_por_hora, "pesos")
print("Horas trabajadas:", horas_trabajadas)
print("Paga:", paga, "pesos")


