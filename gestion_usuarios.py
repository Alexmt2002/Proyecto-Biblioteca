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
        dni = input("Introduce el DNI (7 números + 1 letra): ").upper()
        if re.fullmatch(r"\d{7}[A-Za-z]", dni):
            break
        print("El DNI debe contener 7 números seguidos de 1 letra (ej: 1234567A).")

    
    while True:
        correo = input("Introduce el correo (@gmail.com): ")
        if re.fullmatch(r"[\w\.-]+@gmail\.com", correo):
            break
        print("El correo debe terminar en '@gmail.com'.")

  
    while True:
        tlfno = input("Introduce el teléfono (9 dígitos): ")
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

    print(f"✔ Usuario '{nombre} {apellidos}' creado correctamente.")
    
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
    
                
    
    
    

    
    
            
        