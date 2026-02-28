# Tarea Semana 11: Matriz 5x5 con ingreso por consola
# Programa que crea una matriz de 5x5, solicita valores por teclado y los muestra en forma de tabla

# INICIO
# Crear una matriz de tamaño 5x5
matriz = []

# Para cada fila desde 0 hasta 4:
for fila in range(5):
    fila_nueva = []
    # Para cada columna desde 0 hasta 4:
    for columna in range(5):
        # Pedir al usuario un número
        numero = int(input(f"Ingrese el valor para la posición [{fila}][{columna}]: "))
        # Guardar el número en la matriz
        fila_nueva.append(numero)
    matriz.append(fila_nueva)

# Mostrar "Matriz ingresada:"
print("\nMatriz ingresada:")

# Para cada fila desde 0 hasta 4:
for fila in range(5):
    # Para cada columna desde 0 hasta 4:
    for columna in range(5):
        # Mostrar el valor con formato
        print(f"{matriz[fila][columna]:6}", end="")
    # Saltar de línea
    print()

# FIN
