class Producto:
    def __init__(self, id, nombre, categoria, precio, stock, ventas_totales=0):
        self.id = str(id)
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)
        self.stock = int(stock)
        self.ventas_totales = int(ventas_totales)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
            "ventas_totales": self.ventas_totales
        }