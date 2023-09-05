#Ingrese los coeficientes en una funcion cuadratica y le calcula las raices, si es que estan en los reales
a, b = float(input("Ingrese el coeficiente de X^2\n")), float(input("Ingrese el coeficiente de X\n"))
c = float(input("Ingrese el termino independiente\n"))
if b**2-4*a*c >= 0:
    x1, x2 = (-b+(b**2-4*a*c)**(1/2))/(2*a), (-b-(b**2-4*a*c)**(1/2))/(2*a)
    print(f"\nLas raices son {x1} y {x2}")
else:
    print("\nNo existen raices dentro de los numeros reales con los parametros ingresados")
