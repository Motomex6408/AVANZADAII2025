import os
os.system('cls' if os.name == 'nt' else 'clear')

num1=20
num2=30.5
num1=num1+num2

print("Conversion Implicita")
print(type(num1))
print(type(num2))

print("Conversion explicta")
num1=5.8
print(num1)

edad=input("Ingrese su edad: ")
edad=int(edad)
NuevaEdad=edad+1
print("Nueva edad: ")
print("Vas a cumplir: ", NuevaEdad)
print(type(edad))