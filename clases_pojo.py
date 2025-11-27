class Libro:
    
    ID_libro = 0
    def __init__(self, titulo, autor, anyo, n_pags, genero, editorial, estado="disponible", disponible=True):
        Libro.ID_libro += 1            
        self.id = Libro.ID_libro       
        self.titulo = titulo
        self.autor = autor
        self.anyo = anyo
        self.n_pags = n_pags
        self.genero = genero
        self.editorial = editorial
        self.estado = estado
        self.disponible = disponible
            
    def __str__(self):
        return f"Libro {self.titulo}, autor {self.autor}, {self.n_pags} páginas"
    
    # Getters
    def get_id(self):
        return self.id
    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    def get_anyo(self):
        return self.anyo
    def get_n_pags(self):
        return self.n_pags
    def get_genero(self):
        return self.genero
    def get_editorial(self):
        return self.editorial
    def get_estado(self):
        return self.estado
    def is_disponible(self):
        return self.disponible
    
    # Setters
    def set_titulo(self, titulo):
        self.titulo = titulo
    def set_autor(self, autor):
        self.autor = autor
    def set_anyo(self, anyo):
        self.anyo = anyo
    def set_n_pags(self, n_pags):
        self.n_pags = n_pags
    def set_genero(self, genero):
        self.genero = genero
    def set_editorial(self, editorial):
        self.editorial = editorial
    def set_estado(self, estado):
        self.estado = estado
    def set_disponible(self, disponible):
        self.disponible = disponible


class Usuario:
    
    ID_usuario = 0 
    
    def __init__(self, nombre, apellidos, dni, correo_e, tlfno, direccion, edad):
        Usuario.ID_usuario += 1          
        self.id_usuario = Usuario.ID_usuario
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.correo_e = correo_e
        self.tlfno = tlfno
        self.direccion = direccion
        self.edad = edad

    def __str__(self):
        return f"Usuario {self.id_usuario}: {self.nombre} {self.apellidos}"
    
    # Getters
    def get_id_usuario(self):
        return self.id_usuario
    def get_nombre(self):
        return self.nombre
    def get_apellidos(self):
        return self.apellidos
    def get_dni(self):
        return self.dni
    def get_correo_e(self):
        return self.correo_e
    def get_tlfno(self):
        return self.tlfno
    def get_direccion(self):
        return self.direccion
    def get_edad(self):
        return self.edad
    
    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_apellidos(self, apellidos):
        self.apellidos = apellidos
    def set_dni(self, dni):
        self.dni = dni
    def set_correo_e(self, correo_e):
        self.correo_e = correo_e
    def set_tlfno(self, tlfno):
        self.tlfno = tlfno
    def set_direccion(self, direccion):
        self.direccion = direccion
    def set_edad(self, edad):
        self.edad = edad



class Prestamo:
    
    ID_prestamo = 0  
    
    def __init__(self, id_usuario, id_libro, fecha_inicio, fecha_fin):
        Prestamo.ID_prestamo += 1         
        self.id_prestamo = Prestamo.ID_prestamo
        self.id_usuario = id_usuario
        self.id_libro = id_libro
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.fecha_devolucion = None  

    def __str__(self):
        return f"Préstamo {self.id_prestamo}: Usuario {self.id_usuario} - Libro {self.id_libro}"
    
    # Getters
    def get_id_prestamo(self):
        return self.id_prestamo
    def get_id_usuario(self):
        return self.id_usuario
    def get_id_libro(self):
        return self.id_libro
    def get_fecha_inicio(self):
        return self.fecha_inicio
    def get_fecha_fin(self):
        return self.fecha_fin
    def get_fecha_devolucion(self):
        return self.fecha_devolucion
    
    # Setters
    def set_id_usuario(self, id_usuario):
        self.id_usuario = id_usuario
    def set_id_libro(self, id_libro):
        self.id_libro = id_libro

