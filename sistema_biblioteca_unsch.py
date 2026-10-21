from abc import ABC, abstractmethod


class MaterialBibliografico(ABC):
    def __init__(self, titulo, autor, edicion):
        self.__titulo = titulo
        self.__autor = autor
        self.__edicion = edicion

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def edicion(self):
        return self.__edicion

    @edicion.setter
    def edicion(self, edicion):
        self.__edicion = edicion

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

    @id_multa.setter
    def id_multa(self, id_multa):
        self.__id_multa = id_multa

    @property
    def monto(self):
        return self.__monto

    @monto.setter
    def monto(self, monto):
        self.__monto = monto

    @property
    def motivo(self):
        return self.__motivo

    @motivo.setter
    def motivo(self, motivo):
        self.__motivo = motivo

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

    @fecha_prestamo.setter
    def fecha_prestamo(self, fecha_prestamo):
        self.__fecha_prestamo = fecha_prestamo

    @property
    def fecha_devolucion_esperada(self):
        return self.__fecha_devolucion_esperada

    @fecha_devolucion_esperada.setter
    def fecha_devolucion_esperada(self, fecha_devolucion_esperada):
        self.__fecha_devolucion_esperada = fecha_devolucion_esperada

    @property
    def fecha_devolucion_real(self):
        return self.__fecha_devolucion_real

    @fecha_devolucion_real.setter
    def fecha_devolucion_real(self, fecha_devolucion_real):
        self.__fecha_devolucion_real = fecha_devolucion_real

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

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, correo):
        self.__correo = correo

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

    @materiales.setter
    def materiales(self, materiales):
        self.__materiales = materiales

    def agregarMaterial(self, material):
        self.__materiales.append(material)

    def eliminarMaterial(self, material):
        if material in self.__materiales:
            self.__materiales.remove(material)

    def buscarPorTitulo(self, titulo):
        resultados = []
        for material in self.__materiales:
            if material.titulo.lower() == titulo.lower():
                resultados.append(material)
        return resultados

    def buscarPorAutor(self, autor):
        resultados = []
        for material in self.__materiales:
            if material.autor.lower() == autor.lower():
                resultados.append(material)
        return resultados

    def buscarPorCategoria(self, categoria):
        resultados = []
        for material in self.__materiales:
            if material.__class__.__name__.lower() == categoria.lower():
                resultados.append(material)
        return resultados
