from pathlib import Path
from os import system

main_dir = Path.cwd()

def list_categories():
    i = 0
    for category in main_dir.glob("*"):
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
    return categories[n-1]

def choice_receta(n, category):
    recetas = list(Path(category).glob("*"))
    return recetas[n-1]
    

def read_receta():
    system('cls')
    list_categories()
    category = choice_category(int(input("Seleccione categoría: ")))
    list_recetas(category)
    receta = choice_receta(int(input("Seleccione receta: ")), category)
    file = open(receta)
    print(file.read())
    input("Pulse cualquier tecla para continuar")

def create_categorie():
    Path(input("Escriba el nombre de la nueva categoría: ")).mkdir()

def create_receta():
    system('cls')
    list_categories()
    category = choice_category(int(input("Seleccione categoría: ")))
    nombre_receta = input("Escriba el nombre de la receta: ") + ".txt"
    file = open(Path(category, nombre_receta ) , "w")
    file.write(input("Escriba la receta: "))
    
def delete_categorie():
    system('cls')
    list_categories()
    category = choice_category(int(input("Seleccione categoría: ")))
    print(category)
    Path(category).rmdir()   
    input("Pulse cualquier tecla para continuar")

def delete_receta():
    print("¿Qué receta desea eliminar? \n")
    i = 0
    for receta in Path(main_dir).glob("**/*.txt"):
        i += 1
        print(f" [{i}] - {receta.stem}")
    recetas = list(main_dir.glob("**/*.txt"))
    receta = int(input("Seleccione receta a eliminar: "))
    Path(recetas[receta - 1]).unlink()
    
def count_recetas():
    return len(list(main_dir.glob("**/*.txt")))

def menu():
    print("[1] - leer receta")
    print("[2] - crear receta")
    print("[3] - crear categoría")
    print("[4] - eliminar receta")
    print("[5] - eliminar categoría")
    print("[6] - salir del programa")
    
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

option = "0"

while option != "6":
    print("Bienvenido al RECETARIO")
    print(f"Las recetas se encuentran en {main_dir}")
    print(f"Actualmente hay {count_recetas()} recetas\n")
    menu()
    option = choice_option(input("seleccione una opción:\n "))
    system('cls')
    