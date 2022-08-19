def main():
    print("Mostrando los números pares del 0 al 20:")
    for i in range(1, 21):
        if i % 2 != 0:
            continue
        print(i)
        if i == 10:
            print("¡Paro en 10!")
            break


if __name__ == "__main__":
    main()