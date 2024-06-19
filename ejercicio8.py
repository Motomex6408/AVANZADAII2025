nota1=int(input("Ingrese la primera nota: "))
nota2=int(input("Ingrese la segunda nota: "))
nota3=int(input("Ingrese la Tercera nota: "))
        
promedio= (nota1+nota2+nota3) / 3
        
if promedio >=95:
    print("Felicidades, entraste a los puestos de excelencia academica \n con un promedio de: ", promedio,"%")
else:
    print("Tu notas es: ", promedio,"%")