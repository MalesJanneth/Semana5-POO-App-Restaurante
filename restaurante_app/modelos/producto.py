class Producto:
    def __init__(self,
        nombre: str,
        precio: float,
        cantidad: int,
        disponible: bool
    ):
        #Identificadores decriptivos para almacenar
        #Información del producto
        self.nombre = nombre
        #Tipo de dato numérico
        self.precio = precio
        self.cantidad = cantidad
        #Tipo de dato lógico
        self.disponible = disponible
    def mostrar_informacion(self) ->str:
        #Retorna una cadena de texto con la información del producto
        return (
            f"Nombre: {self.nombre} | "
            f"Precio: {self.precio} | "
            f"Cantidad: {self.cantidad}"
            f"Disponible: {self.disponible}"
        )
    def __str__(self) -> str:

        # Representación en texto del objeto Producto

        return (
            f"{self.tnombre} | "
            f"{self.precio} | "
            f"${self.cantidad}"
        )