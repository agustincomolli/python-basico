def spell(word: str):
    for char in word:
        print(char.upper())

def main():
    name = input("Escribe tu nombre: ")
    spell(name)


if __name__ == "__main__":
    main()
