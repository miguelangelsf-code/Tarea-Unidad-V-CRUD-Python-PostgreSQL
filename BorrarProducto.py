
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


def mostrar_productos():
    cursor.execute(
        "SELECT id_productos, nombre, precio, stock "
        "FROM public.productos ORDER BY id_productos"
    )
    print("Productos en la base de datos:")
    for fila in cursor.fetchall():
        print(fila)
    print("-" * 45)


mostrar_productos()

print("Borrar un Producto")
id_borrar = input("Ingresa el id del producto a borrar: ")

cursor.execute(
    "DELETE FROM public.productos WHERE id_productos = %s",
    (id_borrar,)
)
conexion.commit()
mostrar_productos()

cursor.close()
conexion.close()
print("Conexion cerrada")