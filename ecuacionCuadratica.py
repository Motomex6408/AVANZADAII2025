import os
os.system('cls' if os.name == 'nt' else 'clear')


import math

def discriminante(a, b, c):
    """
    Calculates the discriminant of a quadratic equation.

    Parameters:
        a (float): The coefficient of the quadratic term.
        b (float): The coefficient of the linear term.
        c (float): The constant term.

    Returns:
        float: The discriminant of the quadratic equation.
    """
    discrim = (b**2) - (4*a*c)
    return discrim

def raices(a, b, c):
    """
    Calculates the roots of a quadratic equation.

    Parameters:
        a (float): The coefficient of the quadratic term.
        b (float): The coefficient of the linear term.
        c (float): The constant term.
    """
    discrim = discriminante(a, b, c)
    if discrim < 0:
        print("No hay raices positivas")
    elif discrim == 0:
        print('Solo existe una raiz:', -b / (2*a))
    else:
        raiz1 = (-b + math.sqrt(discrim)) / (2*a)
        raiz2 = (-b - math.sqrt(discrim)) / (2*a)
        print("Las raices son:", raiz1, raiz2)

print('Calculo de raices')
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
raices(a, b, c)