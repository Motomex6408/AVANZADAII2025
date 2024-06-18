import os
os.system('cls' if os.name == 'nt' else 'clear')


lista_1 = ["C","C++","Python","Java"]

lista_2 = ["PHP","SQL","Visual Basic"]

print(lista_1[0])
print(lista_2[0])

print(lista_1)
print(lista_2)

lista12 = lista_1 + lista_2
print(lista12)

lista_3 = ["d","a","c","b","e"]
lista_4 = [5, 4, 7, 1, 9]
lista_5 = [True, False]
lista13 = lista_1 + lista_3
lista14 = lista_1 + lista_4 + lista_5
print(lista13)
print(lista14)
lista_5.append(True)
print(lista_5)

print(lista_5.pop(0))
print(lista_5)

lista_5.sort()
print(lista_5)

lista_5.reverse()
print(lista_5)

print(lista_3[0])


    


