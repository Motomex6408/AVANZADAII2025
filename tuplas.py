import os
os.system('cls' if os.name == 'nt' else 'clear')

mi_tupla = (1, "dos", [3.33,"cuatro", "equis"], (5.0,6))

print(mi_tupla)
print(mi_tupla[0])
print(mi_tupla[2][2])

lista1=list(mi_tupla)
print(lista1)

#Unpacking de tuplas
a, b, c, d = mi_tupla
print(a)
print(b)
print(c)
print(d)

#tupla de pi, e, gravedad
tuplaconst=(3.1416, 2.7182,9.8)
pi,ex,gr=tuplaconst
print("pi: ", pi, "e:", ex, "gravedad: ", gr)

