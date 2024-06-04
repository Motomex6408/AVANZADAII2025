import os
os.system('cls' if os.name == 'nt' else 'clear')

Alumnos = [
    {'ID': 1,'Nombre': 'Anderson Jair Garcia Menjivar', 'Edad': 19},
    {'ID': 2,'Nombre': 'Jorge Arturo Vallecillo Espinoza', 'Edad': 18},
    {'ID': 3,'Nombre': 'Lucas Rodrigo Bautista Juarez', 'Edad': 18},
    {'ID': 4,'Nombre': 'Jose David Mejia Mendoza', 'Edad': 31},
    {'ID': 5,'Nombre': 'Kennet Andersson Martinez Varela', 'Edad': 21},
    {'ID': 6,'Nombre': 'Tomy José Montúfar Zuniga', 'Edad': 19},
    {'ID': 7,'Nombre': 'Ángel Antonio Pérez Rodríguez', 'Edad': 18},
    {'ID': 8,'Nombre': 'José Eduardo Sabillón Hurtado', 'Edad': 19},
    {'ID': 9,'Nombre': 'Diany Lizbeth Enamorado Fernández', 'Edad': 19},
    {'ID': 10,'Nombre': 'Iliana Liceth Zuniga Enamorado', 'Edad': 18},
    {'ID': 11,'Nombre': 'Derick Dair Muñoz Iraheta', 'Edad': 20},
    {'ID': 12,'Nombre': 'Norman Bú', 'Edad': 25},
    {'ID': 13,'Nombre': 'Arnold Stanly Ford', 'Edad': 18},
    {'ID': 14,'Nombre': 'Walter Eduardo Rapalo Smith', 'Edad': 20},
    {'ID': 15,'Nombre': 'Edson Jhair Ríos coto', 'Edad': 26}
]

for Alumno in Alumnos:
    print(Alumno['ID'], Alumno['Nombre'], Alumno['Edad'])
    

