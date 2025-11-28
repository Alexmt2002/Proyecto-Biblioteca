from clases_pojo import Usuario

import os
import csv
import re


ruta = "biblioUsuarios.csv"
encabezado = ["id_usuario", "nombre", "apellidos", "dni", "correo_e", "tlfno", "dirección", "edad"]

if os.path.exists(ruta):
    print()
else:
    with open(ruta,"w", encoding="utf-8",newline="")as file:
        data = csv.writer(file,delimiter=";")
        data.writerow(encabezado)
        
def obtenerSiguienteIdUsuario():
    if not os.path.exists(ruta) or os.path.getsize(ruta) == 0:
        return 1
    with open(ruta, "r", encoding="utf-8") as file:
        dataleer = list(csv.reader(file, delimiter=";"))
        ultimo_id = 0
        for fila in dataleer[1:]:  
            if fila:
                ultimo_id = int(fila[0])
        return ultimo_id + 1


def altaUsuario():
    print("Creación de usuario")

   
    while True:
        nombre = input("Introduce el nombre: ")
        if re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúñÑ ]+", nombre):
            break
        print("El nombre solo puede contener letras.")

   
    while True:
        apellidos = input("Introduce los apellidos: ")
        if re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúñÑ ]+", apellidos):
            break
        print("Los apellidos solo pueden contener letras.")

   
    while True:
        dni = input("Introduce el DNI").upper()
        if re.fullmatch(r"\d{7}[A-Za-z]", dni):
            break
        print("El DNI debe contener 7 números seguidos de 1 letra (ej: 1234567A).")

    
    while True:
        correo = input("Introduce el correo: ")
        if re.fullmatch(r"[\w\.-]+@gmail\.com", correo):
            break
        print("El correo debe terminar en '@gmail.com'.")

  
    while True:
        tlfno = input("Introduce el teléfono: ")
        if re.fullmatch(r"\d{9}", tlfno):
            break
        print("El teléfono debe tener 9 dígitos.")

    
    direccion = input("Introduce la dirección: ")

    
    while True:
        edad = input("Introduce la edad: ")
        if re.fullmatch(r"\d+", edad):
            edad = int(edad)
            break
        print("La edad debe ser un número.")

   
    id_usuario = obtenerSiguienteIdUsuario()

    with open(ruta, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow([id_usuario, nombre, apellidos, dni, correo, tlfno, direccion, edad])

    print(f"Usuario '{nombre} {apellidos}' creado correctamente.")
    
def bajaUsuario():
    dniFuera = input("Introduce el DNI del usuario que quieras dar de baja: ")
    dataNuevo = []

    with open(ruta, "r", encoding="utf-8", newline="") as file:
        dataleer = list(csv.reader(file, delimiter=";"))

    encontrado = False

    for fila in dataleer:
        if fila[3] == dniFuera:
            encontrado = True
            continue
        dataNuevo.append(fila)  

    if not encontrado:
        print(f"No existe ningún usuario con DNI {dniFuera}.")
        return

    
    with open(ruta, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(dataNuevo)

    print(f"Usuario con DNI {dniFuera} dado de baja correctamente.")
    

def modificarUsuario():
    dni_buscar = input("Introduce el DNI del usuario que quieres modificar: ")

    with open(ruta, "r", encoding="utf-8", newline="") as file:
        data = list(csv.reader(file, delimiter=";"))

    encontrado = False

    for i, fila in enumerate(data):
        
        if i == 0:
            continue

        if fila[3] == dni_buscar: 
            encontrado = True
            print("Usuario encontrado. Introduce los nuevos datos (deja vacío para mantener el actual):")

            nuevo_nombre = input(f"Nombre [{fila[1]}]: ") or fila[1]
            nuevo_apellidos = input(f"Apellidos [{fila[2]}]: ") or fila[2]
            nuevo_dni = input(f"DNI [{fila[3]}]: ") or fila[3]
            nuevo_correo = input(f"Correo [{fila[4]}]: ") or fila[4]
            nuevo_tlfno = input(f"Teléfono [{fila[5]}]: ") or fila[5]
            nueva_direccion = input(f"Dirección [{fila[6]}]: ") or fila[6]
            nueva_edad = input(f"Edad [{fila[7]}]: ") or fila[7]

            
            data[i] = [ fila[0],nuevo_nombre, nuevo_apellidos, nuevo_dni, nuevo_correo,
                nuevo_tlfno, nueva_direccion, nueva_edad]

            break

    if not encontrado:
        print(f"No se encontró ningún usuario con DNI '{dni_buscar}'.")
        return

    
    with open(ruta, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(data)

    print(f"Usuario con DNI '{dni_buscar}' modificado correctamente.")

def listarUsuarios():
    with open(ruta, "r", encoding="utf-8", newline="") as file:
        data = list(csv.reader(file, delimiter=";"))
        
        if len(data) <= 1:
            print("No hay usuarios registrados.")
            return
        
        for usuario in data[1:]:  
            print("-----USUARIO------\n"
                f"ID: {usuario[0]} \n"
                f"Nombre: {usuario[1]} \n"
                f"Apellidos: {usuario[2]} \n"
                f"DNI: {usuario[3]} \n"
                f"Correo: {usuario[4]} \n"
                f"Teléfono: {usuario[5]} \n"
                f"Dirección: {usuario[6]} \n"
                f"Edad: {usuario[7]} \n"
                " "
            )

    
                
    
    
    

    
    
            
        