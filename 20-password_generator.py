import random
import string


def generate_password():
    characters = string.ascii_letters
    characters += string.digits
    characters += string.punctuation
    characters += " "

    password = []
    # Elegir 15 caracteres al azar para formar la contraseña.
    for i in range(15):
        password.append(random.choice(characters))
    
    # Convertir lista en un string.
    password = "".join(password)

    return password


def main():
    password = generate_password()
    print(f"Tu nueva contraseña es: '{password}'")


if __name__ == "__main__":
    main()
