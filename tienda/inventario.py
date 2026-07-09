from producto import Producto
from excel_manager import cargar_productos, guardar_productos


class Inventario:

    def __init__(self):
        datos = cargar_productos()
        self.productos = {}

        for p in datos:
            producto = Producto(**p)
            self.productos[producto.id] = producto

    def guardar(self):
        guardar_productos(
            [p.to_dict() for p in self.productos.values()]
        )

    def registrar_producto(self):

        id = input("ID: ")

        if id in self.productos:
            print("Ese ID ya existe.")
            return

        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        self.productos[id] = Producto(
            id,
            nombre,
            categoria,
            precio,
            stock
        )

        self.guardar()

        print("Producto registrado.")

    def actualizar_stock(self):

        id = input("ID: ")

        if id not in self.productos:
            print("Producto no encontrado.")
            return

        cantidad = int(input("Cantidad a agregar: "))

        self.productos[id].stock += cantidad

        self.guardar()

        print("Stock actualizado.")

    def vender_producto(self):

        id = input("ID: ")

        if id not in self.productos:
            print("Producto no existe.")
            return

        cantidad = int(input("Cantidad: "))

        producto = self.productos[id]

        if producto.stock == 0:
            print("No hay stock.")
            return

        if cantidad > producto.stock:
            print("Stock insuficiente.")
            return

        producto.stock -= cantidad
        producto.ventas_totales += cantidad

        if producto.stock < 5:
            print("⚠ ALERTA: Reabastecer producto.")

        self.guardar()

        print("Venta realizada.")

    def cancelar_venta(self):

        id = input("ID: ")

        if id not in self.productos:
            print("Producto no encontrado.")
            return

        cantidad = int(input("Cantidad a cancelar: "))

        producto = self.productos[id]

        if cantidad > producto.ventas_totales:
            print("No se pueden cancelar más ventas que las realizadas.")
            return

        producto.stock += cantidad
        producto.ventas_totales -= cantidad

        self.guardar()

        print("Venta cancelada.")

    def agotados(self):

        agotados = [
            p for p in self.productos.values()
            if p.stock == 0
        ]

        if not agotados:
            print("No hay productos agotados.")
            return

        for p in agotados:
            print(
                p.id,
                p.nombre
            )

    def producto_mas_vendido(self):

        if not self.productos:
            return

        mayor = max(
            self.productos.values(),
            key=lambda p: p.ventas_totales
        )

        print(mayor.nombre, mayor.ventas_totales)

    def ordenar_precio(self, asc=True):

        lista = sorted(
            self.productos.values(),
            key=lambda p: p.precio,
            reverse=not asc
        )

        for p in lista:
            print(
                p.nombre,
                p.precio
            )

    def ordenar_stock(self):

        lista = sorted(
            self.productos.values(),
            key=lambda p: p.stock
        )

        for p in lista:
            print(
                p.nombre,
                p.stock
            )

    def ordenar_ventas(self):

        lista = sorted(
            self.productos.values(),
            key=lambda p: p.ventas_totales,
            reverse=True
        )

        for p in lista:
            print(
                p.nombre,
                p.ventas_totales
            )