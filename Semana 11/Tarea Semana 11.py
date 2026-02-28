# Tarea: Matriz 5x5 con ingreso por consola
# Autor: Malena Ramirez
# Descripción: Programa que solicita al usuario ingresar valores en una matriz 5x5
#              y luego los muestra en formato de tabla

# INICIO
# Crear una matriz de tamaño 5x5
matriz = []

# Para cada fila desde 0 hasta 4
for fila in range(5):
    fila_nueva = []
    # Para cada columna desde 0 hasta 4
    for columna in range(5):
        # Pedir al usuario un número
        numero = int(input(f"Ingrese el valor para la posición [{fila}][{columna}]: "))
        # Guardar el número en la matriz
        fila_nueva.append(numero)
    matriz.append(fila_nueva)

# Mostrar "Matriz ingresada:"
print("\nMatriz ingresada:")
print("-" * 40)

# Para cada fila desde 0 hasta 4
for fila in range(5):
    # Para cada columna desde 0 hasta 4
    for columna in range(5):
        # Mostrar el valor
        print(f"{matriz[fila][columna]:6}", end="")
    # Saltar de línea
    print()

print("-" * 40)
# FIN

