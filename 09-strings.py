print("Trabajando con strings")
name = input("¿Cuál es tu nombre? ")
print(name)
print(f"En mayúsculas: {name.upper()}")
print(f"En minúsculas: {name.lower()}")
print(f"Primera letra en mayúsculas: {name.capitalize()}")
print(f"Cambiando la i por la e: {name.replace('i', 'e')}")
print(f"Letra inicial: {name[0]}")
print(f"Tercer caracter: {name[2]}")
print(f"Cantidad de caracteres: {len(name)}")
print(f"Las 3 primeras letras: {name[:3]}")
print(f"Del 2° caracter al tercero: {name[1:4]}")
print(f"Al reves: {name[::-1]}")