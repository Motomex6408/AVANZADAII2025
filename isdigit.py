import os
os.system('cls' if os.name == 'nt' else 'clear')

mensaje = "Hola1234"
mensaje2 = "hola mundo"
numero = "12345"
decimales = "182345.7896"

#print(mensaje.isdigit())
#print(numero.isdigit())
#print(decimales.isdigit())

#print(mensaje.isnumeric())
#print(numero.isnumeric())
#print(decimales.isnumeric())

#print(mensaje.isdecimal())
#print(numero.isdecimal())
#print(decimales.isdecimal())

# print(mensaje.isalnum())
# print(mensaje2.isalnum())

# mensaje3 = mensaje2.replace("hola", "Hello")

# print(mensaje3)

mensaje4 = "adios mundo cruel"
print(mensaje4.split(" "))

nombre= "Anderson*Jair*Garcia*Menjivar"
print(nombre.split("*"))
print(nombre.count("*"))

nm = nombre.replace("*", " ")
print(nm)