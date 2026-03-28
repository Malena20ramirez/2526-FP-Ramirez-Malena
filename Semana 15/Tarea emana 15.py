# 1. Creación de la colección (Lista vacía)
estudiantes = ["Malena Ramirez", "Luis Campos", "Dhamar Santos"]

# 2. Agregar datos
print("--- Registrando nuevos estudiantes ---")
estudiantes.append("Juan Cedeño")
estudiantes.append("Badillo Marcelo")

# 3. Mostrar la información almacenada (Recorrido)
print("\n--- Lista de Estudiantes Registrados ---")
for i, nombre in enumerate(estudiantes, 1):
    print(f"{i}. {nombre}")

# 4. Operación básica: Buscar un estudiante
print("\n--- Buscando un estudiante en la lista ---")
busqueda = "Luis Campos"
if busqueda in estudiantes:
    print(f"El estudiante '{busqueda}' ya está registrado.")
else:
    print(f"El estudiante '{busqueda}' NO se encuentra en el registro.")

# 5. Operación básica: Eliminar un estudiante
# Supongamos que Luis Campos se retira del curso
print(f"\n--- Eliminando a {busqueda} ---")
estudiantes.remove("Luis Campos")

# Mostrar resultado final
print("Lista actualizada:", estudiantes)