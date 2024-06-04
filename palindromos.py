import os
os.system('cls' if os.name == 'nt' else 'clear')

palabra = input("Ingrese una palabra: ").upper()

if palabra == palabra[::-1]:
    print(palabra + " La palabra es un palíndromo.")
else:
    print(palabra + " La palabra no es un palíndromo.")