from clases_pojo import Libro
import os
import csv

ruta = "biblioLibros.csv"
encabezado = ["ID_libro", "titulo", "autor", "anyo", "n_pags", "genero", "editorial", "estado", "disponible"]

# Crear archivo si no existe
if not os.path.exists(ruta):
    with open(ruta, "w", encoding="utf-8", newline="") as file:
        data = csv.writer(file, delimiter=";")
        data.writerow(encabezado)
    print("Archivo creado.")
else:
    print("El archivo ya existe. No se hizo nada.")


def obtenerSiguienteId():
    if not os.path.exists(ruta) or os.path.getsize(ruta) == 0:
        return 1
    with open(ruta, "r", encoding="utf-8") as file:
        dataleer = list(csv.reader(file, delimiter=";"))
        ultimo_id = 0
        for fila in dataleer[1:]:  
            if fila:
                ultimo_id = int(fila[0])
        return ultimo_id + 1


def agregarLibro():
    
    titulo = input("Introduzca el titulo: ")
    autor = input("Introduzca el autor: ")

    
    while True:
        anyo = input("Introduzca el año (4 dígitos): ")
        if anyo.isdigit() and len(anyo) == 4:
            anyo = int(anyo)
            break
        else:
            print("El año debe ser un número de 4 dígitos.")


    while True:
        n_paginas = input("Introduzca el número de páginas (20 - 1000): ")
        if n_paginas.isdigit():
            n_paginas = int(n_paginas)
            if 20 <= n_paginas <= 1000:
                break
            else:
                print("El número de páginas debe estar entre 20 y 1000.")
        else:
            print("Debe introducir un número válido.")

    genero = input("Introduzca el genero: ")
    editorial = input("Introduzca la editorial: ")

    id_libro = obtenerSiguienteId()
    libroNuevo = Libro(titulo, autor, anyo, n_paginas, genero, editorial)
    libroNuevo.id = id_libro

    with open(ruta, "a", encoding="utf-8", newline="") as file:
        data = csv.writer(file, delimiter=";")
        data.writerow([libroNuevo.id, libroNuevo.titulo, libroNuevo.autor, libroNuevo.anyo,   libroNuevo.n_pags,  libroNuevo.genero,
                       libroNuevo.editorial, libroNuevo.estado, libroNuevo.disponible ])

    print(f"Libro '{libroNuevo.titulo}' agregado correctamente.")

def eliminarLibro():
    titulo = input("Introduce el título del libro que quieras eliminar: ")

    with open(ruta, "r", encoding="utf-8", newline="") as file:
        data = list(csv.reader(file, delimiter=";"))

    data_filtrada = [fila for fila in data if fila[1] != titulo]

    if len(data) == len(data_filtrada):
        print(f"No se encontró ningún libro con el título '{titulo}'.")
    else:
        with open(ruta, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(data_filtrada)
        print(f"El libro '{titulo}' ha sido eliminado correctamente.")


def modificarLibro():
    titulo = input("Introduce el título del libro que quieres modificar: ")

    with open(ruta, "r", encoding="utf-8", newline="") as file:
        data = list(csv.reader(file, delimiter=";"))

    encontrado = False
    for i, fila in enumerate(data):
        if fila[1] == titulo:
            encontrado = True
            print("Libro encontrado. Introduce los nuevos datos (deja vacío para no modificar):")
            nuevo_titulo = input(f"Título [{fila[1]}]: ") or fila[1]
            nuevo_autor = input(f"Autor [{fila[2]}]: ") or fila[2]
            nuevo_anyo = input(f"Año [{fila[3]}]: ") or fila[3]
            nuevo_n_paginas = input(f"Número de páginas [{fila[4]}]: ") or fila[4]
            nuevo_genero = input(f"Género [{fila[5]}]: ") or fila[5]
            nuevo_editorial = input(f"Editorial [{fila[6]}]: ") or fila[6]
            
            data[i] = [
                fila[0], 
                nuevo_titulo,
                nuevo_autor,
                int(nuevo_anyo),
                int(nuevo_n_paginas),
                nuevo_genero,
                nuevo_editorial,
                fila[7],  
                fila[8]   
            ]
            break

    if not encontrado:
        print(f"No se encontró ningún libro con el título '{titulo}'.")
    else:
        with open(ruta, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(data)
        print(f"Libro '{titulo}' modificado correctamente.")
    
def mostrarLibros():
    with open(ruta, "r", encoding="utf-8", newline="") as file:
        data = list(csv.reader(file, delimiter=";"))
        
        if len(data) <= 1:
            print("No hay libros en la biblioteca.")
            return
        
        for libro in data[1:]: 
            print("-----LIBRO------\n"
                f" ID: {libro[0]} \n"
                f"Título: {libro[1]} \n"
                f"Autor: {libro[2]} \n"
                f"Año: {libro[3]} \n"
                f"Páginas: {libro[4]} \n"
                f"Género: {libro[5]} \n"
                f"Editorial: {libro[6]} \n"
                f"Estado: {libro[7]} \n"
                f"Disponible: {libro[8]}\n"
                " "
            )