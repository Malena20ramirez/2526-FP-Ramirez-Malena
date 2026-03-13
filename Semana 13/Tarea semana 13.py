# Método para calcular el total de la compra
def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total

# Uso del método
if __name__ == "__main__":
    precio = 10
    cantidad = 3
    resultado = calcular_total(precio, cantidad)
    print(f"El total de la compra es: {resultado}")