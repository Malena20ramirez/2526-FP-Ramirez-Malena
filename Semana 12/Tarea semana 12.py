# Programa de Reserva de Asientos en una Sala de Cine
# 0 = asiento libre
# 1 = asiento reservado

# Crear matriz 3x4
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Pedir al usuario la fila
print("Ingrese fila (0 a 2):")
f = int(input())

# Pedir al usuario la columna
print("Ingrese columna (0 a 3):")
c = int(input())

# Marcar el asiento como reservado
asientos[f][c] = 1

# Mostrar el estado de la sala
print("Estado de la sala:")

# Usar bucles anidados para mostrar la matriz
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()
