#ecuacionesAritmeticas

import os
os.system('cls' if os.name == 'nt' else 'clear')

a = int(input("Introduce el primer numero: "))
y = int(input("Introduce el segundo numero: "))

if a==0:
    print("Error: 'a' no puede ser 0")
else:
   x= a/y
   print("division: ", round(a/y, 2))
   3
   
print("suma: ", a+y)
print("resta: ", a-y)
print("multiplicacion: ", a*y)
