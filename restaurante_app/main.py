from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():

    # Importación de clases desde otros módulos para reutilizar código organizado

    # CREACIÓN DE OBJETOS PRODUCTO

    producto1 = Producto(
        "Encebollado",
        4.99,
        2,
        True
    )

    producto2 = Producto(
        "Arroz marinero",
        7.25,
        1,
        True
    )


    # CREACIÓN DE OBJETOS CLIENTE

    cliente1 = Cliente(
        "Males Luis",
        "luis@correo.com",
        54,
        True
    )

    cliente2 = Cliente(
        "Conejo Mercedes",
        "mercedes@correo.com",
        50,
        True
    )


    # Creación de un objeto Restaurante

    restaurante = Restaurante()


    # Registro de objetos en las listas del restaurante

    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)

    restaurante.agregar_cliente(cliente1)
    restaurante.agregar_cliente(cliente2)


    # Visualización de la información almacenada en las listas

    print("=== PRODUCTOS REGISTRADOS ===")
    restaurante.mostrar_producto()

    print("\n=== CLIENTES REGISTRADOS ===")
    restaurante.mostrar_clientes()


# Punto de inicio del programa

if __name__ == "__main__":
    main()