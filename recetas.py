import os
from pathlib import Path
from os import system

main_dir = Path(Path.cwd(), "recetas")

def list_categories():
    i = 0
    for category in main_dir.glob("*/"):
        if category.is_dir():
            i += 1
            print(f" [{i}] - {category.name}")

def list_recetas(category):
    i = 0
    for receta in Path(category).glob("*"):
        i += 1
        print(f" [{i}] - {receta.stem}")

def choice_category(n):
    all = list(main_dir.glob("*/"))
    categories = [obj for obj in all if obj.is_dir()]
    return categories[int(n)-1]

def choice_receta(n, category):
    recetas = list(Path(category).glob("*"))
    return recetas[int(n)-1]
    
def read_receta():
    system('cls')
    list_categories()
    n = 'x'
    while not n.isnumeric() or int(n) not in range(1, (count_categories() + 1)):
        n = input("Seleccione categoría: ")
    category = choice_category(n)
    if len(list(category.glob("**/*.txt"))) == 0:
        print("No hay recetas en esta categoría")
        input("Pulse una tecla para continuar...")
        init()
    list_recetas(category)
    n = 'x'
    while not n.isnumeric() or int(n) not in range(1, (len(list(category.glob("**/*.txt"))) + 1)):
        n = input("Seleccione receta: ")
    receta = choice_receta(n, category)
    file = open(receta)
    print(file.read())
    input("Pulse cualquier tecla para continuar")

def create_categorie():
    categoria = input("Escriba el nombre de la nueva categoría: ")
    if not os.path.exists(Path("recetas", categoria)):
        Path("recetas", categoria).mkdir()
    else:
        print("La categoría ya existe")
        input("Pulse una tecla para continuar")

def create_receta():
    system('cls')
    list_categories()
    n = '8'
    while not n.isnumeric() or int(n) not in range(1, (count_categories() + 1)):
        n = input("Seleccione categoría: ")
    category = choice_category(n)
    nombre_receta = input("Escriba el nombre de la receta: ") + ".txt"
    if not os.path.exists(Path(category, nombre_receta )):
        file = open(Path(category, nombre_receta ) , "w")
        file.write(input("Escriba la receta: "))
    else:
        print("La receta ya existe.")
        input("Pulse una tecla para volver a intentarlo")
    
def delete_categorie():
    system('cls')
    list_categories()
    n = '8'
    while not n.isnumeric() or int(n) not in range(1, (count_categories() + 1)):
        n = input("Seleccione categoría: ")
    category = choice_category(n)
    print(category)
    if len(list(category.glob("**/*.txt"))) == 0:
        Path("recetas", category).rmdir()
        print("Categoría borrada") 
    else:
        print("El directorio no está vacío.")
        print("No se puede eliminar") 
    input("Pulse cualquier tecla para continuar")

def delete_receta():
    print("¿Qué receta desea eliminar? \n")
    i = 0
    for receta in Path(main_dir).glob("**/*.txt"):
        i += 1
        print(f" [{i}] - {receta.stem}")
    recetas = list(main_dir.glob("**/*.txt"))
    receta = '0'
    while not receta.isnumeric() or int(receta) not in range(1, count_recetas() + 1):
        receta = input("Seleccione receta a eliminar: ")
    Path(recetas[int(receta) - 1]).unlink()
    
def count_recetas():
    return len(list(main_dir.glob("**/*.txt")))

def count_categories():
    return len(list(main_dir.glob("*/")))

def menu():
    print('''
    [1] - leer receta
    [2] - crear receta
    [3] - crear categoría
    [4] - eliminar receta
    [5] - eliminar categoría
    [6] - salir del programa\n
    ''')
    
def choice_option(option):
    match option:
        case "1":
         read_receta()
        case "2":
         create_receta()
        case "3":
            create_categorie()
        case "4":
            delete_receta()
        case "5":
            delete_categorie()
        case "6":
            pass    
        case _:
            print("Opción incorrecta")
            input("Pulse cualquier tecla para volver a intentarlo")
    return option

def init():
    system('cls')
    option = "0"
    while option != "6":
        print('*' * 45)
        print("*" * 10 + " Bienvenido al RECETARIO " + "*" * 10)
        print('*' * 45 + "\n")
        print(f"Las recetas se encuentran en {main_dir}\n")
        print(f"Actualmente hay {count_recetas()} recetas\n")
        menu()
        option = choice_option(input("seleccione una opción:\n "))
        system('cls')

init()