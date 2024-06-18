#Impirmir 10 valores con while
import os
os.system('cls' if os.name == 'nt' else 'clear')


# i=0

# while i<10:
#     print(i)
#     i+=1

# print("Ingresa S para salir")

# while True:
#     entrada=input("Ingrese S para salir ")
#     if entrada.upper() == 'S':
#         break


# print("Ciclo controlado por bandera 2")
# bandera= "x"
# while bandera != 's':
#     bandera=input("Ingrese S para salir ")


print("Ciclo controlado por baderin")
bandera = True
while bandera != False:
    bandera = input("Ingresa S para Salir: ")
    print(bandera.upper())
    salir=bandera.upper()
    if salir == 'S':
        bandera = False
        print("Saliste del ciclo")
    