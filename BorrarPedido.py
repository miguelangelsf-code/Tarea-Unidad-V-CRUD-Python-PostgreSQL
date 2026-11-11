
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


def mostrar_pedidos():
    cursor.execute(
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
    print("Pedidos en la base de datos:")
    for fila in cursor.fetchall():
        print(fila)
    print("-" * 45)


mostrar_pedidos()

print("Borrar un Pedido")
id_borrar = input("Ingresa el id del pedido a borrar: ")

cursor.execute(
    "DELETE FROM public.pedidos WHERE id_pedido = %s",
    (id_borrar,)
)
conexion.commit()

mostrar_pedidos()

cursor.close()
conexion.close()
print("Conexion cerrada")