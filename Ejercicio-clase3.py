# ¿Qué información debe proporcionar la resolución del problema?
#   Imprimir el sueldo correspondiente a un empleado

# ¿Qué datos se necesitan para resolver el problema? Si los tengo ¿Cuáles son?
#   Costo por hora del empleado
#   Horas trabajadas por el empleado

# ¿Qué pasos debo realizar para llegar a la resolución del problema? 
#   Crear una funcion que realize un calculo (multiplicación) entre las horas trabajadas y el costo de la hora.
#   Pedir el costo de la hora y las horas que trabajo el empleado
#   Ingresar los datos a la funcion
#   imprimir por consola el resultado

def CalcularSueldo(cantidadHora, precioHora) :
    resultado = cantidadHora * precioHora

    print("Sueldo correspondiente:")
    print("$",resultado)

print("✋✋  Bienvenido  ✋✋")
print("Ingrese la cantidad de Horas que trabajo el empleado:")
cantidadHora = int(input())
print("Ingrese el precio de la hora:")
precioHora = int(input())
print("")
CalcularSueldo(cantidadHora, precioHora)