catalog = []
unique_categories = set()

print("======================================")
print("BIENVENIDO AL SISTEMA DE CATÁLOGO V1.0")
print("======================================")

item_id = input("Introduce el ID de la pieza: ")
name = input("Introduce el nombre del pieza: ")
price = float(input("Introduce el precio del pieza: "))

print(type(price))

#category = input("Introduce la categoria del pieza: ")
#status = input("Introduce el estado del pieza: ")
#description = input("Introduce la descripcion del pieza: ")

item = {
    "id": item_id,
    "name": name,
    "price": price
}

print(item)