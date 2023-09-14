"""Datos:
Largo del terreno: pedirlo
Ancho del terrreno: pedirlo
Precio por metro: pedirlo

Calcular:
Superficie del terreno= largo * ancho
precio_total = superficie * precio

Condiciones:
-Si tiene mas de 400m2 se hace un 10% de descuento
-Si el valor del terreno supera los $25.000 se le hace un 5%

Opciones de condiciones:                 Descuento:
-Superficie > 400 & supere los $25.000     (15%)
-Superficie > 400 & no supere los $25.000  (10%)
-Superficie < 400 & supere los $25.000     (05%)
-Superficie < 400 & no supere los $25.000  (00%)"""

try:
    largo = float(input("Ingrese el lago de su terreno en metros: "))
    ancho = float(input("Ingrese el ancho de su terreno en metros: "))
    precio = float(input("Ingrese el precio del metro cuadrado del terreno: "))
    superficie = largo * ancho
    total = superficie * precio
    if superficie > 400 and total > 25000:
        descuento = total * 0.85
        print("El precio del terreno con descuentos es de: $", descuento)
        print("Ya que el terreno posee el descuento de: \n -10% por superficie mayor a 400m2 \n -05% por costar más de $25.000")
    if superficie > 400 and total < 25000:
        descuento = total * 0.90
        print("El precio del terreno con descuentos es de: $", descuento)
        print("Ya que el terreno posee el descuento de: \n -10% por superficie mayor a 400m2")
    if superficie < 400 and total > 25000:
        descuento = total * 0.95
        print("El precio del terreno con descuentos es de: $", descuento)
        print("Ya que el terreno posee el descuento de: \n -05% por costar más de $25.000")
    if superficie < 400 and total < 25000:
        print("El precio del terreno es de: $", total)
        print("El terreno no cuenta con descuento ya que tiene: \n -Superficie menor a 400m2 \n -Cuesta menos $25.000")
except ValueError:
    print("Ingrese un valor numerico")