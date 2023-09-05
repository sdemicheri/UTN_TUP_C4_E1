#Pedir informacion
horas_trabajo = input("⌚Ingrese cuantas horas de trabajo realizo este mes⌚ : ")
costo_hora = input("💵Ingrese cual es el costo por hora de trabajo💵 : ")

#Imprimir informacion, realizar calculo, mensaje con el sueldo

sueldo = int(horas_trabajo)*int(costo_hora)
print(f"Su sueldo de este mes es: ${sueldo}")