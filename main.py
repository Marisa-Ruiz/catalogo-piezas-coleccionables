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
    unique_categories.add(category)

print(f"\nEl catálogo contiene {len(catalog)} piezas registradas.")

print("\n===== CATÁLOGO COMPLETO =====")
for piece in catalog:
    print(f"\nID: {piece['id']}")
    print(f"Nombre: {piece['name']}")
    print(f"Categoría: {piece['category']}")
    print(f"Precio: {piece['price']}")
    print(f"Estado: {piece['status']}")
    print(f"Descripción: {piece['description']}")

print(f"\nCategorías registradas: {unique_categories}")
print(f"Cantidad de categorías diferentes: {len(unique_categories)}")

print("\n===== PIEZAS DISPONIBLES =====")
found = False
for piece in catalog:
    if piece['status'] == "disponible":
        print(f"- {piece['id']}: {piece['name']} ({piece['price']})")
        found = True
if not found:
    print("No hay piezas disponibles.")

print("\n===== PIEZAS RESERVADAS =====")
found = False
for piece in catalog:
    if piece['status'] == "reservada":
        print(f"- {piece['id']}: {piece['name']} ({piece['price']})")
        found = True
if not found:
    print("No hay piezas reservadas.")

print("\n===== PIEZAS VENDIDAS =====")
found = False
for piece in catalog:
    if piece['status'] == "vendida":
        print(f"- {piece['id']}: {piece['name']} ({piece['price']})")
        found = True
if not found:
    print("No hay piezas vendidas.")

print("\n===== FILTRAR POR PRECIO MÍNIMO =====")

valid_price = False
while not valid_price:
    min_price_input = input("Introduce un precio mínimo: ")
    if min_price_input.replace(".", "", 1).isdigit():
        min_price = float(min_price_input)
        valid_price = True
    else:
        print("Debes introducir un valor numérico.")

found = False
for piece in catalog:
    if piece['price'] > min_price:
        print(f"- {piece['id']}: {piece['name']} ({piece['price']})")
        found = True

if not found:
    print(f"No hay piezas con precio superior a {min_price}.")

print("\n===== REGLA DE PUBLICACIÓN =====")
for piece in catalog:
    can_publish = piece['price'] > 0 and piece['status'] == "disponible"
    print(f"- {piece['id']}: {piece['name']} -> ¿Se puede publicar? {can_publish}")

print("\n===== REGLA DE REVISIÓN =====")
for piece in catalog:
    needs_review = piece['status'] == "reservada" or piece['status'] == "vendida"
    print(f"- {piece['id']}: {piece['name']} -> ¿Requiere revisión? {needs_review}")

print("\n===== PIEZAS NO VENDIDAS =====")
for piece in catalog:
    if piece['status'] != "vendida":
        print(f"- {piece['id']}: {piece['name']} ({piece['status']})")

print("\n===== MANIPULACIÓN DE STRINGS =====")

first_piece = catalog[0]

# 1. Mostrar info usando concatenación
print("Concatenación: " + first_piece['name'] + " - " + first_piece['category'])

# 2. Mostrar info usando interpolación (f-string)
print(f"Interpolación: {first_piece['name']} - {first_piece['category']}")

# 3. Solicitar etiquetas separadas por comas
tags_input = input("\nIntroduce etiquetas separadas por comas (ej: retro,anime,limited): ")

# 4. Convertir la cadena en elementos separados
tags_list = tags_input.split(",")
print(f"Etiquetas como lista: {tags_list}")

# 5. Reemplazar 'usada' por 'certificada' en una descripción
updated_description = first_piece['description'].replace("usada", "certificada")
print(f"Descripción actualizada: {updated_description}")

# 6. Solicitar un nombre de usuario
username = input("\nIntroduce tu nombre de usuario: ")

# 7. Mostrar el nombre en varios formatos
print(f"Sin espacios: '{username.strip()}'")
print(f"En minúsculas: {username.lower()}")
print(f"En mayúsculas: {username.upper()}")
print(f"En formato título: {username.title()}")

# 8. Normalizar el nombre de una pieza antes de mostrarlo
normalized_name = first_piece['name'].strip().title()
print(f"\nNombre de pieza normalizado: {normalized_name}")