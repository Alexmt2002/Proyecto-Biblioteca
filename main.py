from gestion_libros import *
from gestion_usuarios import *
 
def main():
    
    print("1. Gestión Libros\n2. Gestión usuarios\n3. Registrar préstamo\n4. Registrar devolución\n5. Listados de préstamos\n6. Salir")
    opcion = int(input("Escoge la opción que quieras realizar: "))
    
    while opcion != 6:
        if opcion == 1:
            # --- SUBMENÚ LIBROS ---
            opcionLibro = 0
            while opcionLibro != 5:
                print("\n1. Agregar Libro\n2. Eliminar Libro\n3. Modificar Libro\n4. Monstrar todos los libros\n5. Atrás")
                opcionLibro = int(input("Escoge la opción que quieras realizar: "))

                if opcionLibro == 1:
                    agregarLibro()
                elif opcionLibro == 2:
                    eliminarLibro()
                elif opcionLibro == 3:
                    modificarLibro()
                elif opcionLibro == 4:
                    mostrarLibros()
                elif opcionLibro == 5:
                    print("Volviendo al menú principal...\n")
                else:
                    print("Opción no válida")

       
        elif opcion == 2:
            opcionUsuario = 0
            while opcionUsuario != 5:
                print("\n1. Agregar Usuario\n2. Eliminar Usuario\n3. Modificar Usuario\n4. Monstrar todos los Usuario\n5. Atrás")
                opcionUsuario = int(input("Escoge la opción que quieras realizar: "))

                if opcionUsuario == 1:
                    altaUsuario()
                elif opcionUsuario == 2:
                    bajaUsuario()
                elif opcionUsuario == 3:
                    modificarUsuario()
                elif opcionUsuario == 4:
                    modificarUsuario()
                elif opcionUsuario == 5:
                    print("Volviendo al menú principal...\n")
                else:
                    print("Opción no válida")

        print("1. Gestión Libros\n2. Gestión usuarios\n3. Registrar préstamo\n4. Registrar devolución\n5. Listados de préstamos\n6. Salir")
        opcion = int(input("Escoge la opción que quieras realizar: "))

    print("¡Programa finalizado!")

main()