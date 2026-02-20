# Tarea Semana 10: Matriz y creación de cuenta en GitHub
# Parte 1: Programa con matriz

# Declarar matriz de 3x3 con números enteros
matriz = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]

# Códigos ANSI para colores
ROJO = '\033[91m'
VERDE = '\033[92m'
AZUL = '\033[94m'
AMARILLO = '\033[93m'
RESET = '\033[0m'

# Recorrer la matriz con ciclos anidados e imprimir los valores
print("Valores de la matriz 3x3:")
print()

colores = [ROJO, VERDE, AZUL]

for i in range(3):
    print(colores[i], end="")
    for j in range(3):
        print(f"matriz[{i}][{j}] = {matriz[i][j]}", end="  ")
    print(RESET)  # Salto de línea después de cada fila

print()
print("Otra forma de imprimir la matriz:")
print()

# Forma alternativa: imprimir la matriz de manera más visual con colores
for i, fila in enumerate(matriz):
    print(colores[i] + str(fila) + RESET)
