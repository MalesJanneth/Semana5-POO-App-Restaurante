class Restaurante:
    def __init__(self):

        # Estructuras de datos compuestas (listas) para almacenar múltiples objetos

        self.producto = []
        self.ciente = []

    def agregar_producto(self, producto) -> None:

        # Agrega un objeto Producto a la lista

        self.producto.append(producto)

    def agregar_cliente(self, cliente) -> None:

        # Agrega un objeto Cliente a la lista

        self.cliente.append(cliente)

    def mostrar_producto(self) -> None:

        # Recorre la lista de productos y muestra cada objeto almacenado

        for producto in self.producto:
            print(producto)

    def mostrar_clientes(self) -> None:

        # Recorre la lista de clientes y muestra cada objeto almacenado

        for cliente in self.cleiente:
            print(cliente)