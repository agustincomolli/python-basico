def convert_to_dollars(amount_money, dollar_value):
    return round(amount_money / dollar_value, 2)


argentinian_money = 135.75
colombian_money = 4, 396.67
mexican_money = 20.19
menu = """
Bienvenido al conversor de monedas 馃挵

1 - Pesos argentinos
2 - Pesos colombianos
3 - Pesos mexicanos

Elija una opci贸n: """

option = int(input(menu))

amount_money = float(input("驴Cu谩nto dinero quieres cambiar? "))

if option == 1:
    # Convertir pesos argentinos a d贸lares.
    dollars = convert_to_dollars(argentinian_money, amount_money)
elif option == 2:
    # Convertir pesos colombianos a d贸lares.
    dollars = convert_to_dollars(colombian_money, amount_money)
elif option == 3:
    # Convertir pesos mexicanos a d贸lares.
    dollars = convert_to_dollars(mexican_money, amount_money)
else:
    print("El valor ingresado no es una opci贸n v谩lida.")
    exit()

print(f"Son u$s {dollars} 馃挼")
