catalog = []
unique_categories = set()

print("======================================")
print("BIENVENIDO AL SISTEMA DE CATÁLOGO V1.0")
print("======================================")

for i in range(10):
    item_id = input("Introduce el ID de la pieza: ")
    name = input("Introduce el nombre del pieza: ")
    price = float(input("Introduce el precio del pieza: "))
    category = input("Introduce la categoria del pieza: ")
    status = input("Introduce el estado del pieza: ")
    description = input("Introduce la descripcion del pieza: ")

    item = {
        "id": item_id,
        "name": name,
        "price": price,
        "category": category,
        "status": status,
        "description": description
    }

    catalog.append(item)

print(f"\nEl catálogo contiene {len(catalog)} piezas registradas.")

print("\nIDs registrados en el catálogo:")
for piece in catalog:
    print(f"- {piece['id']}: {piece['name']}")
