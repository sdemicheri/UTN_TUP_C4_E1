# creo las variables
def calcular_paga(horas_trabajadas, costo_por_hora):
    try:
        horas_trabajadas = float(horas_trabajadas)
        costo_por_hora = float(costo_por_hora)

        if horas_trabajadas < 0 or costo_por_hora < 0:
            return "Los valores ingresados deben ser números positivos."

        paga = horas_trabajadas * costo_por_hora
        return f"El pago que le corresponde es: ${paga}"
    except ValueError:
        return "Por favor, ingresa valores numéricos válidos."


#imprimo las variables
def main():
    print("Calculadora de Pagos para empresa")
    print("====================")

    horas_trabajadas = input("Ingrese el número de horas trabajadas: ")
    costo_por_hora = input("Ingrese el costo por hora: ")

    resultado = calcular_paga(horas_trabajadas, costo_por_hora)
    print(resultado)


if __name__ == "__main__":
    main()
