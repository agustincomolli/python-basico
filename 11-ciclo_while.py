def main():
    # Definir una constante.
    LIMIT = 1000

    count = 0
    power_two = 2 ** count
    while power_two < LIMIT:
        print(f"2 elevado a {count} es {power_two}")
        count += 1
        power_two = 2 ** count


if __name__ == "__main__":
    main()
