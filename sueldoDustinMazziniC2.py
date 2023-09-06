def calcular_sueldo_neto(sueldo, porcentaje_descuento):
    descuento = (sueldo * porcentaje_descuento) // 100  # Usamos división entera para el descuento
    sueldo_neto = sueldo - descuento
    return sueldo_neto


sueldo1 = int(input("Ingrese el sueldo del empleado 1: "))
porcentaje_descuento1 = int(input("Ingrese el porcentaje de descuento para el empleado 1: "))

sueldo2 = int(input("Ingrese el sueldo del empleado 2: "))
porcentaje_descuento2 = int(input("Ingrese el porcentaje de descuento para el empleado 2: "))

sueldo3 = int(input("Ingrese el sueldo del empleado 3: "))
porcentaje_descuento3 = int(input("Ingrese el porcentaje de descuento para el empleado 3: "))


sueldo_neto1 = calcular_sueldo_neto(sueldo1, porcentaje_descuento1)
sueldo_neto2 = calcular_sueldo_neto(sueldo2, porcentaje_descuento2)
sueldo_neto3 = calcular_sueldo_neto(sueldo3, porcentaje_descuento3)


print("Sueldo Neto del Empleado 1:", sueldo_neto1)
print("Sueldo Neto del Empleado 2:", sueldo_neto2)
print("Sueldo Neto del Empleado 3:", sueldo_neto3)
