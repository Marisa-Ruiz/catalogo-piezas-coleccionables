# Sistema de Catálogo de Piezas Coleccionables

## Objetivo del programa
Este proyecto es un programa de consola en Python que permite gestionar un
catálogo básico de piezas coleccionables. El programa permite registrar piezas,
consultar la información del catálogo, aplicar filtros por estado y precio,
aplicar reglas de negocio mediante operadores lógicos, y manipular datos de
tipo texto (strings).

## Contexto del catálogo
El catálogo reúne 10 piezas coleccionables de temática variada: videojuegos,
anime, cine y repostería (un catálogo personal de objetos de colección
inspirados en distintos universos ficticios). Cada pieza tiene un identificador,
nombre, categoría, precio, estado (disponible, reservada o vendida) y una
descripción.

## Funcionalidades implementadas
- Registro de 10 piezas coleccionables mediante captura de datos por terminal.
- Almacenamiento de las piezas en una lista de diccionarios (`catalog`).
- Registro de categorías únicas usando un `set`.
- Visualización del catálogo completo con todos los campos de cada pieza.
- Filtrado de piezas por estado (disponible, reservada, vendida).
- Filtrado de piezas por precio mínimo, con validación numérica.
- Aplicación de reglas de negocio con operadores lógicos (`and`, `or`, `!=`):
  regla de publicación, regla de revisión y piezas no vendidas.
- Manipulación de strings: concatenación, interpolación, `split`, `replace`,
  `strip`, `lower`, `upper`, `title`.

## Ejemplo de interacción

======================================
BIENVENIDO AL SISTEMA DE CATÁLOGO V1.0

Introduce el ID de la pieza: VJ-01
Introduce el nombre del pieza: Espada Llave Espada
Introduce el precio del pieza: 89.99
Introduce la categoria del pieza: Videojuegos
Introduce el estado del pieza: disponible
Introduce la descripcion del pieza: Réplica oficial certificada de Kingdom Hearts.
...

===== CATÁLOGO COMPLETO =====

ID: VJ-01
Nombre: Espada Llave Espada
Categoría: Videojuegos
Precio: 89.99
Estado: disponible
Descripción: Réplica oficial certificada de Kingdom Hearts.
...

Categorías registradas: {'Videojuegos', 'Anime', 'Cine', 'Repostería'}
Cantidad de categorías diferentes: 4

===== PIEZAS DISPONIBLES =====

VJ-01: Espada Llave Espada (89.99)
...

===== REGLA DE PUBLICACIÓN =====

VJ-01: Espada Llave Espada -> ¿Se puede publicar? True
...

## Tecnologías utilizadas
- Python 3.x
- PyCharm IDE

## Cómo ejecutar el programa
1. Clona este repositorio: `git clone <url-del-repo>`
2. Entra en la carpeta del proyecto: `cd catalogo-piezas-coleccionables`
3. Ejecuta el archivo principal: `python main.py`
4. Introduce los datos solicitados por terminal para cada una de las 10 piezas.
