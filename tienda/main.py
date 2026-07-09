from inventario import Inventario

inventario = Inventario()

while True:

    print("""
1 Registrar producto
2 Actualizar stock
3 Vender
4 Cancelar venta
5 Productos agotados
6 Producto más vendido
7 Ordenar por precio ASC
8 Ordenar por precio DESC
9 Ordenar por stock
10 Ordenar por ventas
0 Salir
""")

    op = input("Opción: ")

    if op == "1":
        inventario.registrar_producto()

    elif op == "2":
        inventario.actualizar_stock()

    elif op == "3":
        inventario.vender_producto()

    elif op == "4":
        inventario.cancelar_venta()

    elif op == "5":
        inventario.agotados()

    elif op == "6":
        inventario.producto_mas_vendido()

    elif op == "7":
        inventario.ordenar_precio(True)

    elif op == "8":
        inventario.ordenar_precio(False)

    elif op == "9":
        inventario.ordenar_stock()

    elif op == "10":
        inventario.ordenar_ventas()

    elif op == "0":
        break

    else:
        print("Opción inválida.")