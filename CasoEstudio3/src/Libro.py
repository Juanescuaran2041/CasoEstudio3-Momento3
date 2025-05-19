__author__ = "Juan Esteban Cuaran Santander"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "juan.cuaran@campusucc.edu.co"

from Transacciones import Transacciones, Tipo
class Libro:

    def __init__(self, ISBN:str, Titulo:str, precioCompra:float, precioVenta:float, CantidadActual:int):
        self.__ISBN = ISBN
        self.__Titulo = Titulo
        self.__precioCompra = precioCompra
        self.__precioVenta = precioVenta
        self.__CantidadActual = CantidadActual
        self.__Transacciones = []
        self.__observadores = []

    #################################
    ## get and set
    #################################

    def get_ISBN (self):
        return self.__ISBN
    
    def get_Titulo (self):
        return self.__Titulo
    
    def get_precioCompra (self):
        return self.__precioCompra
    
    def get_precioVenta (self):
        return self.__precioVenta
    
    def get_CantidadActual (self):
        return self.__CantidadActual
    
    def get_Transacciones (self):
        return self.__Transacciones
    
    def set_ISBN (self, nuevoISBN:str):
        self.__ISBN = nuevoISBN
    
    def set_Titulo (self, nuevoTitulo:str):
        self.__Titulo = nuevoTitulo

    def set_precioCompra (self, nuevoPrecioCompra:float):
        self.__precioCompra =nuevoPrecioCompra
    
    def set_precioVenta (self, nuevoPrecioVenta:float):
        self.__precioVenta = nuevoPrecioVenta
    
    def set_CantidadActual (self, nuevaCantidad:int):
        self.__CantidadActual = nuevaCantidad

    #########################
    ## methods
    #########################

    def registrarTransaccion (self, TipoT:Tipo, Fecha:str, cantidad:int):
        nuevaTransaccion = Transacciones(TipoT, Fecha, cantidad)
        self.__Transacciones.append(nuevaTransaccion)

        if TipoT == Tipo.ABASTECIMIENTO:
            self.__CantidadActual += cantidad
        else:
            self.__CantidadActual -= cantidad

        self.notificador()

    def contadorAbastecimiento(self):
        Contador = 0
        for i in self.__Transacciones:
            if i.get_Tipo() == Tipo.ABASTECIMIENTO:
                Contador += 1

        return Contador
    
    def totalVendidos(self):
        total = 0
        for transaccion in self.__Transacciones:
            if transaccion.get_Tipo() == Tipo.VENTA:
                total += transaccion.get_CantidadEjemplares()
            
        return total
    

    #########################
    #Methods observers
    #########################

    def agregarObservador (self, observador):
        self.__observadores.append(observador) 
    
    def notificador (self):
        for observador in self.__observadores:
            observador.actualizar (self)
    
#########################
# Observadores y programacion reactiva tradicional
######################### 

class ObservadorCantidad:
    def actualizar(self, libro):
        print(f"[Cantidad actualizada] '{libro.get_Titulo()}': {libro.get_CantidadActual()} unidades disponibles.")

class ObservadorVenta:
    def actualizar(self, libro):
        ultimaTransaccion = libro.get_Transacciones()[-1]
        if ultimaTransaccion.get_Tipo() == Tipo.VENTA:
            print(f"[Venta realizada] Se vendieron {ultimaTransaccion.get_CantidadEjemplares()} unidades de '{libro.get_Titulo()}'. Total vendidos: {libro.totalVendidos()}.")

class ObservadorAbastecimiento:
    def actualizar(self, libro):
        UltimaTransaccion = libro.get_Transacciones()[-1]
        if UltimaTransaccion.get_Tipo() == Tipo.ABASTECIMIENTO:
            print(f"[Abastecimiento realizado] Se abastecieron {UltimaTransaccion.get_CantidadEjemplares()} unidades de '{libro.get_Titulo()}'. Total abastecimientos: {libro.contadorAbastecimiento()}.")