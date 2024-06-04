import os
os.system('cls' if os.name == 'nt' else 'clear')

c = int(input("Bienvenido a Computadoras Motomex, Ingrese cuantas Computadoras va a comprar: "))
precio = 16000
if c >= 10:
    d = (c * precio) * 0.20
    print("Felicidades obtuviste descuento de 20% por tu compra, el prcio total a pagar es: ", d)
    print("Gracias por su compra")
if c > 1000:
    d = (c * precio) * 0.50
    print("Felicidades obtuviste descuento de 50% por tu compra, el precio total a pagar es: ", d) 
    print("Gracias por su compra")   
else:
    d= c * precio
    print("Total a pagar es de: ", d)
    print("Gracias por su compra")