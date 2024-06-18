import os
os.system('cls' if os.name == 'nt' else 'clear')

# for i in range(10):
#     print(i)
 
#for inicio, fin, incremento   
# for i in range(2, 22, 2):
#     print(i)
    
#ciclo for con listas
lista=["uno","dos","tres","cuatro","cinco"]
# for item in lista:
#     print(item)

#invertir lista
for item in reversed(lista):
    print(item)

#ciclo for tuplas
# tupla=("uno","dos","tres","cuatro","cinco")
# for item in tupla:
#     print(item)

#ciclo for diccionarios
diccionario={
    "curso": "PYTHON Total",
     "Clase": "Ciclos",
     "Tema": "For",
     "Duracion": "1 trimestre",
     "Profesor": "Anderson Jair Garcia"
 }
print(diccionario)
for LLave in reversed (diccionario):
    print(LLave, ": ", diccionario[LLave])