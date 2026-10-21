from abc import ABC, abstractmethod


class MaterialBibliografico(ABC):
    def __init__(self, titulo, autor, edicion):
        self.__titulo = titulo
        self.__autor = autor
        self.__edicion = edicion

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def edicion(self):
        return self.__edicion

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_edicion(self):
        return self.__edicion

    @abstractmethod
    def verificarDisponibilidad(self):
        pass

    @abstractmethod
    def solicitarPrestamo(self):
        pass


class Libro(MaterialBibliografico):
    def verificarDisponibilidad(self):
        return True

    def solicitarPrestamo(self):
        return True


class Revista(MaterialBibliografico):
    def verificarDisponibilidad(self):
        return True

    def solicitarPrestamo(self):
        return True


class Tesis(MaterialBibliografico):
    def verificarDisponibilidad(self):
        return True

    def solicitarPrestamo(self):
        return True


class Multa:
    def __init__(self, id_multa, monto, motivo):
        self.__id_multa = id_multa
        self.__monto = monto
        self.__motivo = motivo

    @property
    def id_multa(self):
        return self.__id_multa

    @property
    def monto(self):
        return self.__monto

    @property
    def motivo(self):
        return self.__motivo

    def get_id_multa(self):
        return self.__id_multa

    def get_monto(self):
        return self.__monto

    def get_motivo(self):
        return self.__motivo

    def calcularMulta(self):
        return self.__monto

    def pagar(self):
        return True


class Prestamo:
    def __init__(self, fecha_prestamo, fecha_devolucion_esperada, fecha_devolucion_real=None):
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion_esperada = fecha_devolucion_esperada
        self.__fecha_devolucion_real = fecha_devolucion_real

    @property
    def fecha_prestamo(self):
        return self.__fecha_prestamo

    @property
    def fecha_devolucion_esperada(self):
        return self.__fecha_devolucion_esperada

    @property
    def fecha_devolucion_real(self):
        return self.__fecha_devolucion_real

    def get_fecha_prestamo(self):
        return self.__fecha_prestamo

    def get_fecha_devolucion_esperada(self):
        return self.__fecha_devolucion_esperada

    def get_fecha_devolucion_real(self):
        return self.__fecha_devolucion_real

    def registrarPrestamo(self):
        return True

    def finalizarPrestamo(self):
        return True


class Usuario:
    def __init__(self, id_usuario, nombre, apellido, correo):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo

    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def correo(self):
        return self.__correo

    def get_id_usuario(self):
        return self.__id_usuario

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_correo(self):
        return self.__correo

    def buscarMaterial(self, titulo):
        pass

    def realizarPrestamo(self, material):
        pass

    def pagarMulta(self, multa):
        pass


class Estudiante(Usuario):
    pass


class Docente(Usuario):
    pass


class PersonalAdministrativo(Usuario):
    pass


class Bibliotecario(Usuario):
    def gestionarCatalogo(self):
        pass

    def gestionarUsuarios(self):
        pass

    def procesarPrestamos(self):
        pass


class Catalogo:
    def __init__(self):
        self.__materiales = []

    @property
    def materiales(self):
        return self.__materiales

    def get_materiales(self):
        return self.__materiales

    def buscarPorTitulo(self, titulo):
        return [m for m in self.__materiales if m.titulo == titulo]

    def buscarPorAutor(self, autor):
        return [m for m in self.__materiales if m.autor == autor]

    def buscarPorCategoria(self, categoria):
        pass