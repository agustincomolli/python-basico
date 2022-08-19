def check_prime_number(number):
    count = 0

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        else:
            if number % i == 0:
                count += 1
    if count == 0:
        return True
    else:
        return False


def main():
    number = int(input("Escribe un número: "))
    if check_prime_number(number):
        print("Es un número primo.")
    else:
        print("No es un número primo.")


if __name__ == "__main__":
    main()
