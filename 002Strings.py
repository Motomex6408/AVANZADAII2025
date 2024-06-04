import os
os.system('cls' if os.name == 'nt' else 'clear')

saludo = "Ho1l4a5_8m8u8n8d8o"


try:
    print(saludo.index('o',4,7))
except ValueError:
    print("No se encontro la subcadena")

print(saludo.rindex('o'))

print(saludo[0:4])

cedula = "1601200500023"
departamento=cedula[0:2]
print(departamento)
municipio=cedula[2:4]
print(municipio)

#islower( )
print("hola".islower())

#isupper( )
print("HOLA".isupper())

print(saludo[2:6])
print(saludo[2::2])

print(saludo[::-1])
print(saludo[::1])