from abc import ABC, abstractmethod


class MaterialBibliografico(ABC):
    def __init__(self, titulo, autor, edicion):
        self.__titulo = titulo
        self.__autor = autor
        self.__edicion = edicion
        self.__disponible = True

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, valor):
        self.__titulo = valor

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, valor):
        self.__autor = valor

    @property
    def edicion(self):
        return self.__edicion

    @edicion.setter
    def edicion(self, valor):
        self.__edicion = valor

    @property
    def disponible(self):
        return self.__disponible

    @disponible.setter
    def disponible(self, valor):
        self.__disponible = valor

    def verificarDisponibilidad(self):
        return self.__disponible

    def solicitarPrestamo(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False


class Libro(MaterialBibliografico):
    pass


class Revista(MaterialBibliografico):
    pass


class Tesis(MaterialBibliografico):
    pass


class Multa:
    def __init__(self, id_multa, monto, motivo):
        self.__id_multa = id_multa
        self.__monto = monto
        self.__motivo = motivo

    @property
    def id_multa(self):
        return self.__id_multa

    @id_multa.setter
    def id_multa(self, valor):
        self.__id_multa = valor

    @property
    def monto(self):
        return self.__monto

    @monto.setter
    def monto(self, valor):
        self.__monto = valor

    @property
    def motivo(self):
        return self.__motivo

    @motivo.setter
    def motivo(self, valor):
        self.__motivo = valor

    def calcularMulta(self):
        return self.__monto

    def pagar(self):
        return True


class Prestamo:
    def __init__(self, fecha_prestamo, fecha_devolucion_esperada, fecha_devolucion_real):
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion_esperada = fecha_devolucion_esperada
        self.__fecha_devolucion_real = fecha_devolucion_real

    @property
    def fecha_prestamo(self):
        return self.__fecha_prestamo

    @fecha_prestamo.setter
    def fecha_prestamo(self, valor):
        self.__fecha_prestamo = valor

    @property
    def fecha_devolucion_esperada(self):
        return self.__fecha_devolucion_esperada

    @fecha_devolucion_esperada.setter
    def fecha_devolucion_esperada(self, valor):
        self.__fecha_devolucion_esperada = valor

    @property
    def fecha_devolucion_real(self):
        return self.__fecha_devolucion_real

    @fecha_devolucion_real.setter
    def fecha_devolucion_real(self, valor):
        self.__fecha_devolucion_real = valor

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
    def id_usuario(self, valor):
        self.__id_usuario = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, valor):
        self.__apellido = valor

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        self.__correo = valor

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
    def materiales(self, valor):
        self.__materiales = valor

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


if __name__ == "__main__":
    catalogo = Catalogo()
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "1ra")
    catalogo.agregarMaterial(libro1)

    print("Libro agregado:", libro1.titulo)
    print("Disponible:", libro1.verificarDisponibilidad())
    print("Solicitar préstamo:", libro1.solicitarPrestamo())
    print("Disponible tras préstamo:", libro1.verificarDisponibilidad())