from producto import Producto


class Inventario:

    def __init__(self):
        self.productos = {}

    def registrar_producto(self):
        id = input("ID: ")

        if id in self.productos:
            print("Ese ID ya existe.")
            return

        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        self.productos[id] = Producto(id, nombre, categoria, precio, stock)

        print("Producto registrado correctamente.")

    def actualizar_stock(self):
        id = input("ID del producto: ")

        if id not in self.productos:
            print("Producto no encontrado.")
            return

        cantidad = int(input("Cantidad a agregar: "))

        if cantidad <= 0:
            print("Cantidad inválida.")
            return

        self.productos[id].stock += cantidad

        print("Stock actualizado.")

    def vender_producto(self):
        id = input("ID del producto: ")

        if id not in self.productos:
            print("Producto no encontrado.")
            return

        producto = self.productos[id]

        cantidad = int(input("Cantidad: "))

        if cantidad <= 0:
            print("Cantidad inválida.")
            return

        if producto.stock == 0:
            print("No se puede vender. Producto agotado.")
            return

        if cantidad > producto.stock:
            print("Stock insuficiente.")
            return

        producto.stock -= cantidad
        producto.ventas_totales += cantidad

        print("Venta realizada.")

        if producto.stock < 5:
            print("ALERTA: Stock menor a 5 unidades.")

    def cancelar_venta(self):
        id = input("ID del producto: ")

        if id not in self.productos:
            print("Producto no encontrado.")
            return

        producto = self.productos[id]

        cantidad = int(input("Cantidad a cancelar: "))

        if cantidad <= 0:
            print("Cantidad inválida.")
            return

        if cantidad > producto.ventas_totales:
            print("No es posible cancelar esa cantidad.")
            return

        producto.stock += cantidad
        producto.ventas_totales -= cantidad

        print("Venta cancelada.")

    def agotados(self):
        agotados = [p for p in self.productos.values() if p.stock == 0]

        if not agotados:
            print("No hay productos agotados.")
            return

        print("\nProductos agotados")

        for p in agotados:
            print(p)

    def producto_mas_vendido(self):
        if not self.productos:
            print("No hay productos.")
            return

        producto = max(
            self.productos.values(),
            key=lambda x: x.ventas_totales
        )

        print("\nProducto más vendido:")
        print(producto)

    def ordenar_por_precio(self, asc=True):
        lista = sorted(
            self.productos.values(),
            key=lambda x: x.precio,
            reverse=not asc
        )

        for p in lista:
            print(p)

    def ordenar_por_stock(self):
        lista = sorted(
            self.productos.values(),
            key=lambda x: x.stock
        )

        for p in lista:
            print(p)

    def ordenar_por_ventas(self):
        lista = sorted(
            self.productos.values(),
            key=lambda x: x.ventas_totales,
            reverse=True
        )

        for p in lista:
            print(p)

    def mostrar_catalogo(self):
        if not self.productos:
            print("Inventario vacío.")
            return

        for producto in self.productos.values():
            print(producto)