
import psycopg2

conexion = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='comercio',
    user='postgres',
    password='******'
)

cursor = conexion.cursor()
print("Conexion exitosa a la base de datos")
print("-" * 45)

pedidos_nuevos = [
    (1, 1, 2),
    (2, 2, 1),
    (3, 3, 3),
    (4, 4, 2),
]

cursor.executemany(
    'INSERT INTO pedidos (id_clientes, id_productos, cantidad) VALUES (%s, %s, %s)',
    pedidos_nuevos
)

total_insertados = cursor.rowcount
conexion.commit()

print(f"{total_insertados} pedidos insertados de una sola vez")
print("-" * 45)

cursor.execute(
    """
    SELECT
        p.id_pedido,
        c.nombre AS cliente,
        pr.nombre AS producto,
        p.cantidad,
        p.fecha
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

print("-" * 45)

cursor.close()
conexion.close()
print("Conexion cerrada")
