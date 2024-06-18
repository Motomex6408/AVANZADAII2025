import os
os.system('cls' if os.name == 'nt' else 'clear')

factorial = int(input("Introduce un numero: "))
resultado = 1

for i in range(1, factorial+1):
    resultado *= i
    
print(f"{factorial}! = {resultado}")