def give_welcome():
    print("¡Hola! Bienvenido a Python.")


def give_message(message):
    print("Hola, cómo estás?")
    print(message)
    print("Adiós")


menu = """
1 - Opción 1
2 - Opción 2
3 - Opción 3

Elige una opción: """

option = int(input(menu))
if option == 1:
    give_message("Elegiste la opción 1")
elif option == 2:
    give_message("Elegiste la opción 2")
elif option == 3:
    give_message("Elegiste la opción 3")
else:
    give_message("¡No elegiste NADA!")
