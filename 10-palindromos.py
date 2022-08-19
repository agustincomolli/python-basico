def check_palindrome(word_to_check: str):
    # Eliminar los espacios en blanco.
    word_to_check = word_to_check.replace(" ", "")
    # Poner la palabra en minúsculpa.
    word_to_check = word_to_check.lower()
    # Invertir la palabra.
    reverse_word = word_to_check[::-1]

    if word_to_check == reverse_word:
        return True
    else:
        return False


def main():
    word = input("Escribe una palabra: ")
    es_palindromo = check_palindrome(word)
    if es_palindromo:
        print("¡Es un palíndromo! 🥳")
    else:
        print("No es un palíndromo 😢")


if __name__ == "__main__":
    main()
