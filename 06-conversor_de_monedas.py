# 1 dólar es equivalente a: 
argentinian_money = 135.75
colombian_money = 4,396.67
mexican_money = 20.19
dollars = 0

menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos argentinos
2 - Pesos colombianos
3 - Pesos mexicanos

Elija una opción: """

option = int(input(menu))

amount_money = float(input("¿Cuánto dinero quieres cambiar? "))

if option == 1:
    # Convertir pesos argentinos a dólares.
    dollars = round(amount_money / argentinian_money, 2)
elif option == 2:
    # Convertir pesos colombianos a dólares.
    dollars = round(amount_money / colombian_money, 2)
elif option == 3:
    # Convertir pesos mexicanos a dólares.
    dollars = round(amount_money / mexican_money, 2)
else:
    print("El valor ingresado no es una opción válida.")
    exit()

print(f"Son u$s {dollars} 💵")
