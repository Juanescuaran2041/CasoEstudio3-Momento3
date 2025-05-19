__author__ = "Juan Esteban Cuaran Santander"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "juan.cuaran@campusucc.edu.co"

from Transacciones import Transacciones, Tipo
from datetime import datetime
from Libro import Libro

class Tienda:
    def __init__(self, libros:list[Libro],DineroCaja:float):
        self.__libros = []
        assert libros is not None
        for libro in libros:
            if isinstance(libro, Libro): #libro es una instancia de Libro
                self.__libros.append(libro)

        self.__dineroCaja = DineroCaja
        self.__observadores = []
            
    def RegistrarLibro (self, ISBN:str, Titulo:str, PrecioCompra:float, PrecioVenta:float):
        cantidadActual = 1 #Por el momento
        nuevoLibro = Libro(ISBN,Titulo,PrecioCompra,PrecioVenta, cantidadActual)
        self.__libros.append(nuevoLibro)
    
    def EliminarLibro (self, ISBN:str):
        for libro in self.__libros:
            assert any(libro.get_ISBN() == ISBN), "Libro no encontrado"

        self.__libros = [libro for libro in self.__libros if libro.get_ISBN() != ISBN]

        
    def BuscarLibroTitulo (self, Titulo:str):
        for libro in self.__libros:
            if libro.get_Titulo() == Titulo:
                return libro
    

    def BuscarLibroISBN (self, ISBN:str):
        for libro in self.__libros:
            if libro.get_ISBN () == ISBN:
                return libro
    
    def AbastecerEjemplares (self,ISBN:str, cantidad:int):
        fecha = datetime.now().strftime("%d/%m/%Y")
        for libro in self.__libros:
            if ISBN == libro.get_ISBN ():
                self.__dineroCaja -= libro.get_precioCompra() * cantidad
                libro.registrarTransaccion(Tipo.ABASTECIMIENTO, fecha, cantidad)

                self.notificador()
                
    def VenderEjemplares (self, ISBN:str, cantidad:int):
        fecha = datetime.now().strftime("%d/%m/%Y")
        for libro in self.__libros:
            if ISBN == libro.get_ISBN ():
                self.__dineroCaja += libro.get_precioVenta() * cantidad
                libro.registrarTransaccion (Tipo.VENTA, fecha, cantidad)

                self.notificador()
    
    def ContarAbastecimientos (self, ISBN:str):
        for libro in self.__libros:
            if ISBN == libro.get_ISBN ():
                libro.contadorAbastecimiento()

    def BuscarLibroMasCostoso (self):
        assert len(self.__libros) > 0, "No hay Libros registrados"
        Libro_Costoso = self.__libros[0]
        for libro in self.__libros:
            if libro.get_precioVenta () > Libro_Costoso.get_precioVenta ():
                Libro_Costoso = libro
        
        return Libro_Costoso

    def BuscarLibroMasEconomico (self):
        assert len(self.__libros) > 0, "No hay libros registrados"
        Libro_Economico = self.__libros [0]
        for libro in self.__libros:
            if libro.get_precioVenta () < Libro_Economico.get_precioVenta ():
                Libro_Economico = libro
        
        return Libro_Economico
    
    def BuscarLibroMasVendido (self):
        assert len(self.__libros) > 0, "No hay libros registrados "

        libro_mas_vendido = self.__libros [0]
        masventas = libro_mas_vendido.totalVendidos()

        for libro in self.__libros[1:]:
            ventas = libro.totalVendidos()
            if ventas > masventas:
                masventas = ventas
                libro_mas_vendido = libro

        return libro_mas_vendido
    
    def get_DineroCaja (self):
        return self.__dineroCaja
    
    def asignarObservador (self, observador):
        self.__observadores.append(observador)

    def notificador (self):
        for observador in self.__observadores:
            observador.actualizar(self)

    ######################
    # Observadores
    ######################

class ObservadorDineroCaja:
    def actualizar(self, tienda):
        print(f"[Dinero en caja actualizado]: ${tienda.get_DineroCaja()}")
