from styles import Style

arbitroPrincipal = input("Ingrese el nombre del árbitro principal: ")
arbitroDeLinea1 = input("Ingrese el nombre del árbitro de linea 1: ")
arbitroDeLinea2 = input("Ingrese el nombre del tercer árbitro de linea2: ")
arbitroSuplente = input("Ingrese el nombre del cuarto árbitro suplente: ")
cancha = input("Ingrese la cancha donde se realizará el partido")
fecha = input("Ingrese la fecha (dd/mm/aa): ")
hora = input("Ingrese la hora (24hs): ")


def add_style_to_text(style, text):
    return style + text + Style.END


def print_referees_names():
    print(add_style_to_text(Style.YELLOW,
                            "\t⚽Árbitro principal: {0} "
                            "\n\t🚩Árbitro De Linea 1: {1} "
                            "\n\t🚩Árbitro De Linea 2: {2} "
                            "\n\t👤Árbitro Suplente: {3}"
                            .format(arbitroPrincipal, arbitroDeLinea1, arbitroDeLinea2, arbitroSuplente)))


def print_match_data():
    print(add_style_to_text(Style.BOLD + Style.BLUE,
                            "\t⚽Cancha: {0} "
                            "\n\t🚩Fecha: {1} "
                            "\n\t🚩Hora del partido: {2} "
                            .format(cancha, fecha, hora)))


print("-" * 40)
print('''\n ''', add_style_to_text(Style.UNDERLINE, "Ticket con información del partido:"))
print_referees_names()
print("#" * 40)
print_match_data()
print("-" * 40)
