def main():
    products = {
        "leche": 120,
        "salsa": 380,
        "yerba": 560,
        "azúcar": 180
    }

    print(f"El precio de la yerba es: ${products['yerba']}")

    print(f"\nLista de precios: \n{'*' * 18}")
    for key, value in products.items():
        print(f"{key.capitalize()} - $ {value}")

    print(f"\nLista de productos: \n{'*' * 20}")
    for product in products.keys():
        print(product.capitalize())


if __name__ == "__main__":
    main()
