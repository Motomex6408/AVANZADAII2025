import os
os.system('cls' if os.name == 'nt' else 'clear')

numero = int(input("Introduce un numero: "))

for i in range(1, 11):
    print(numero , " X ", i , " = ", numero * i)