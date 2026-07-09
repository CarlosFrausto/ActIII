from inventario import Inventario

inventario = Inventario()

while True:

    print("\n====== TIENDA ======")
    print("1. Registrar producto")
    print("2. Actualizar stock")
    print("3. Procesar venta")
    print("4. Cancelar venta")
    print("5. Mostrar agotados")
    print("6. Producto más vendido")
    print("7. Ordenar por precio")
    print("8. Ordenar por stock")
    print("9. Ordenar por ventas")
    print("10. Mostrar catálogo")
    print("0. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        inventario.registrar_producto()

    elif opcion == "2":
        inventario.actualizar_stock()

    elif opcion == "3":
        inventario.vender_producto()

    elif opcion == "4":
        inventario.cancelar_venta()

    elif opcion == "5":
        inventario.agotados()

    elif opcion == "6":
        inventario.producto_mas_vendido()

    elif opcion == "7":
        orden = input("Ascendente (A) o Descendente (D): ").upper()

        if orden == "A":
            inventario.ordenar_por_precio(True)
        else:
            inventario.ordenar_por_precio(False)

    elif opcion == "8":
        inventario.ordenar_por_stock()

    elif opcion == "9":
        inventario.ordenar_por_ventas()

    elif opcion == "10":
        inventario.mostrar_catalogo()

    elif opcion == "0":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")