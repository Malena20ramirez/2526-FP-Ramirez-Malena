def calcularTotal(precio, cantidad):
    """
    Método que calcula el total de una compra
    Args:
        precio: precio unitario del producto
        cantidad: cantidad de productos
    Returns:
        el total de la compra
    """
    total = precio * cantidad
    return total


def main():
    """Programa principal"""
    print("===== CALCULADORA DE COMPRAS =====")

    # Solicitar el precio del producto
    precio = float(input("Ingrese el precio unitario del producto: $"))

    # Solicitar la cantidad
    cantidad = int(input("Ingrese la cantidad de productos: "))

    # Calcular el total
    total = calcularTotal(precio, cantidad)

    # Mostrar los resultados
    print("\n===== DETALLES DE LA COMPRA =====")
    print(f"Precio unitario: ${precio:.2f}")
    print(f"Cantidad: {cantidad}")
    print(f"TOTAL A PAGAR: ${total:.2f}")


if __name__ == "__main__":
    main()