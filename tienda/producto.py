class Producto:
    def __init__(self, id, nombre, categoria, precio, stock):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.ventas_totales = 0

    def __str__(self):
        return (
            f"ID: {self.id} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock} | "
            f"Ventas: {self.ventas_totales}"
        )