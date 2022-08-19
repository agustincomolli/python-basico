def main():
    name = "Agustín"
    is_working = True
    age = 45
    email = "agustíncomolli@gmail.com"
    user = []

    # Agregar un valor a la lista
    user.append(1)
    user.append(name)
    user.append(is_working)
    user.append(age)
    user.append(email)
    user.append("Esto se borrará")
    
    print(user[1])  # Mostrar el 1° valor.
    print(user[-1]) # Mostrar el último valor.
    user.pop(-1)    # Eliminar el último valor.

    # Recorrer la lista y mostrar su contenido.
    for item in user:
        print(item)


if __name__ == "__main__":
    main()