from datetime import datetime
from Transacciones import Tipo
from Libro import Libro, ObservadorCantidad, ObservadorVenta, ObservadorAbastecimiento
from Tienda import Tienda, ObservadorDineroCaja

def main():
    # Crear libros
    libro1 = Libro("978-3-16-148410-0", "El Ingenioso Hidalgo", 20000.0, 35000.0, 10)
    libro2 = Libro("978-0-262-13472-9", "Programación en Python", 25000.0, 45000.0, 5)

    # Agregar observadores a libros
    libro1.agregarObservador(ObservadorCantidad())
    libro1.agregarObservador(ObservadorVenta())
    libro1.agregarObservador(ObservadorAbastecimiento())

    libro2.agregarObservador(ObservadorCantidad())
    libro2.agregarObservador(ObservadorVenta())
    libro2.agregarObservador(ObservadorAbastecimiento())

    # Crear tienda con libros y dinero en caja inicial
    tienda = Tienda([libro1, libro2], 100000.0)
    tienda.asignarObservador(ObservadorDineroCaja())

    # Probar abastecimiento
    print(" Abastecer libro 1 con 5 ejemplares")
    tienda.AbastecerEjemplares("978-3-16-148410-0", 5)

    # Probar venta
    print(" Vender 3 ejemplares del libro 2")
    tienda.VenderEjemplares("978-0-262-13472-9", 3)

    # Mostrar libro más costoso
    libro_costoso = tienda.BuscarLibroMasCostoso()
    print(f"Libro más costoso: {libro_costoso.get_Titulo()} a ${libro_costoso.get_precioVenta()}")

    # Mostrar libro más vendido
    libro_mas_vendido = tienda.BuscarLibroMasVendido()
    print(f"Libro más vendido: {libro_mas_vendido.get_Titulo()} con {libro_mas_vendido.totalVendidos()} ventas")

if __name__ == "__main__":
    main()
