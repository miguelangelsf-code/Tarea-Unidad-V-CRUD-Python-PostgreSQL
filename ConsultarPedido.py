
import psycopg2

conexion = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='comercio',
    user='postgres',
    password="TU_CONTRASEÑA"
)

cursor = conexion.cursor()
print("Conexion exitosa a la base de datos")
print("-" * 45)

cursor.execute(
    # Muestra la lista de pedidos con el nombre del cliente,
    # el producto solicitado, la cantidad y la fecha.
    # También ordena los pedidos por su código.

    """
    SELECT p.id_pedido, c.nombre AS cliente,
           pr.nombre AS producto, p.cantidad, p.fecha
    FROM public.pedidos p
    INNER JOIN public.clientes c
        ON p.id_clientes = c.id_clientes
    INNER JOIN public.productos pr
        ON p.id_productos = pr.id_productos
    ORDER BY p.id_pedido
    """
)
print("Pedidos en la base de datos")

for fila in cursor.fetchall():
    print(fila)

print("*" * 45)
print("Modificar los Datos del Pedido")
id_modificar = input("Ingresa el Código del Pedido: ")
nueva_cantidad = input("Ingresa la nueva Cantidad del Pedido: ")

cursor.execute(
    "UPDATE pedidos SET cantidad = %s WHERE id_pedido = %s",
    (nueva_cantidad, id_modificar)
)
conexion.commit()

print("-" * 45)
cursor.execute(
    # Muestra los pedidos con los nombres de los clientes y productos,
    # junto con la cantidad y la fecha.
    # Ordena la lista por el código de cada pedido.
    # Permite ver los datos actualizados después de la modificación.
    """
    SELECT p.id_pedido, c.nombre AS cliente,
           pr.nombre AS producto, p.cantidad, p.fecha
    FROM public.pedidos p
    INNER JOIN public.clientes c
        ON p.id_clientes = c.id_clientes
    INNER JOIN public.productos pr
        ON p.id_productos = pr.id_productos
    ORDER BY p.id_pedido
    """
)
print("Pedidos en la base de datos")

for fila in cursor.fetchall():
    print(fila)

print("Datos Actualizados")
print("*" * 45)

cursor.close()
conexion.close()
print("Conexion cerrada")