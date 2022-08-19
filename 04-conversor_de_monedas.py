# Conversor de pesos argentinos a dólares.
amount_money = float(input("Pesos $ a convertir: "))
dollar_value = 135.75
amount_dollars = amount_money / dollar_value
# Redondear a dos decimales.
amount_dollars = round(amount_dollars, 2)
print(f"Son: {amount_dollars} u$s.")

# Conversosr de dólares a pesos argentinos.
amount_money = float(input("Dólares u$s a convertir: "))
dollar_value = 135.75
amount_pesos = amount_money * dollar_value
amount_pesos = round(amount_pesos, 2)
print(f"Son $ {amount_pesos}")
