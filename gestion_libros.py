from clases_pojo import Libro
import os 
import csv


ruta = "biblioLibros.csv"
encabezado = [ "ID_libro", "titulo", "autor", "anyo", "n_pags", "genero", "editorial", "estado", "disponible"]


if not os.path.exists(ruta):
    with open(ruta, "w", encoding="utf-8", newline="") as file:
        data = csv.writer(file, delimiter=";")
        escribir = data.writerow(encabezado)
    print("Archivo creado.")
else:
    print("El archivo ya existe. No se hizo nada.")
    


def agregarLibro():
    titulo = input("Introduzca el titulo: ")
    autor = input("Introduzca el autor: ")
    anyo = int(input("Introduzca el año: "))
    n_paginas = int(input("Introduzca el numero de paginas: "))
    genero = input("Introduzca el genero: ")
    editorial = input("Introduzca la editorial: ")
    
    libroNuevo = Libro(titulo, autor, anyo, n_paginas, genero, editorial)
    
    with open(ruta, "a", encoding="utf-8", newline="") as file:
        data = csv.writer(file, delimiter=";")
        data.writerow([
            libroNuevo.id,
            libroNuevo.titulo,
            libroNuevo.autor,
            libroNuevo.anyo,
            libroNuevo.n_pags,
            libroNuevo.genero,
            libroNuevo.editorial,
            libroNuevo.estado,
            libroNuevo.disponible
        ])
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
    titulo = input("Introduce del libro que quieres modificar: ")
    
    
    
    
    
    
    
    
    
    

    
