# Lista con números y cadenas
datos = [
    [101, "manzana", 3.5],
    ["leche", 42, "queso"],
    [7, "galletas", "pan"],
    ["Queso", 8, "Mermelada"]
]

# Mostrar toda la lista
print("Contenido de la lista:")
for i in range(len(datos)):
    print(f"Sublista {i + 1}: {datos[i]}")

# Entrada del usuario
entrada = input("\nIngrese el valor a buscar (número o texto): ").lower()

encontrado = False

# Buscar en todas las sublistas
for i in range(len(datos)):
    # for j in range(len(datos[i])):
        item = datos[i][0]
        if str(item).lower() == entrada:
            print(
                f"\n'{entrada}' fue encontrado en la sublista {i + 1}: {datos[i]}")
            encontrado = True
            break  # Salta a la siguiente sublista si ya encontró coincidencia

if not encontrado:
    print(f"\n'{entrada}' no fue encontrado en ninguna sublista.")
