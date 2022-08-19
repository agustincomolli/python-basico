def main():
    print("Imprimir 10 números")
    
    print("Con ciclo while: ")
    count = 0
    while count < 10:
        print(count + 1)
        count += 1

    print("Con ciclo for:")
    for i in range(1, 11):
        print(i)


if __name__ == "__main__":
    main()