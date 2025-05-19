__author__ = "Juan Esteban Cuaran Santander"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "juan.cuaran@campusucc.edu.co"

from enum import Enum, auto

class Tipo (Enum):
    ABASTECIMIENTO = auto()
    VENTA = auto()

class Transacciones:

    def __init__ (self, Tipo:Tipo, Fecha:str, CantidadEjemplares:int):
        self.__Tipo = Tipo
        self.__Fecha:str = Fecha
        self.__CantidadEjemplares:int = CantidadEjemplares

    __method__ = "get_Tipo"
    __params__ = "None"
    __returns__ = "TipoTransaccion"
    __description__ = "Metodo que retorna el tipo de transaccion"

    def get_Tipo (self) -> Tipo:
        return self.__Tipo

    __method__ = "get_Fecha"
    __params__ = "None"
    __returns__ = "Fecha"
    __description__ = "Metodo que retorna la fecha de la transaccion"

    def get_Fecha (self) -> str:
        return self.__Fecha
    
    __method__ = "get_CantidadEjemplares"
    __params__ = "None"
    __returns__ = "CantidadEjemplares"
    __description__ = "Metodo que retorna la cantidad de ejemplares de la transaccion"

    def get_CantidadEjemplares (self) ->int:
        return self.__CantidadEjemplares

    __method__ = "set_Tipo"
    __params__ = "nuevoTipo"
    __returns__ = "None"
    __description__ = "Metodo que permite cambiar el tipo de transaccion realizada"

    def set_Tipo (self, nuevoTipo): 
        assert nuevoTipo in Tipo
        self.__Tipo = nuevoTipo

    __method__ = "set_Fecha"
    __params__ = "nuevaFecha"
    __returns__ = "none"
    __description__ = "Metodo que permite cambiar la fecha de la transaccion"
    
    def set_Fecha (self, nuevaFecha:str):
        self.__Fecha = nuevaFecha

    __method__ = "set_CantidadEjemplares"
    __params__ = "nuevaCantidad"
    __returns__ = "None"
    __description__ = "Metodo que permite cambiar la cantidad de ejemplares de la transaccion"

    def set_CantidadEjemplares (self, nuevaCantidad:int):
        self.__CantidadEjemplares = nuevaCantidad
