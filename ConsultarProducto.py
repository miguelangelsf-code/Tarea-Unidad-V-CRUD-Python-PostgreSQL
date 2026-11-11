
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

cursor.execute(
    "SELECT id_productos, nombre, precio, stock "
    "FROM public.productos ORDER BY id_productos"
)
print("Productos en la base de datos")

for fila in cursor.fetchall():
    print(fila)

print("*" * 45)
print("Modificar los Datos del Producto")
id_modificar = input("Ingresa el Código del Producto: ")
nuevo_precio = input("Ingresa el nuevo Precio del Producto: ")

cursor.execute(
    "UPDATE productos SET precio = %s WHERE id_productos = %s",
    (nuevo_precio, id_modificar)
)
conexion.commit()

print("-" * 45)
cursor.execute(
    "SELECT id_productos, nombre, precio, stock "
    "FROM public.productos ORDER BY id_productos"
)
print("Productos en la base de datos")

for fila in cursor.fetchall():
    print(fila)

print("Datos Actualizados")
print("*" * 45)

cursor.close()
conexion.close()
print("Conexion cerrada")
