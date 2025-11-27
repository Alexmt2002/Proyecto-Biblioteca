from gestion_libros import *
 
def main():
    
    print("1. Gestión Libros\n2. Gestión usuarios\n3. Registrar préstamo\n4. Registrar devolución\n5. Listados de préstamos\n6. Salir")
    opcion = int(input("Escoge la opción que quieras realizar: "))
    
    while opcion != 6:
        if opcion == 1:
            # --- SUBMENÚ LIBROS ---
            opcionLibro = 0
            while opcionLibro != 4:
                print("\n1. Agregar Libro\n2. Eliminar Libro\n3. Modificar Libro\n4. Atrás")
                opcionLibro = int(input("Escoge la opción que quieras realizar: "))

                if opcionLibro == 1:
                    agregarLibro()
                elif opcionLibro == 2:
                    eliminarLibro()
                elif opcionLibro == 3:
                    modificarLibro()
                elif opcionLibro == 4:
                    print("Volviendo al menú principal...\n")
                else:
                    print("Opción no válida")

        # Aquí podrás seguir con los demás menús:
        # elif opcion == 2: ...

        print("1. Gestión Libros\n2. Gestión usuarios\n3. Registrar préstamo\n4. Registrar devolución\n5. Listados de préstamos\n6. Salir")
        opcion = int(input("Escoge la opción que quieras realizar: "))

    print("¡Programa finalizado!")

main()