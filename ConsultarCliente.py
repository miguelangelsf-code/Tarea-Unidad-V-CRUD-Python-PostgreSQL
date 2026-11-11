import psycopg2

conexion = psycopg2.connect (
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
    "SELECT id_clientes, nombre, email, ciudad, fecha_alta "
    "FROM public.clientes ORDER BY id_clientes"
)
print("Clientes en la base de datos")

for fila in cursor.fetchall():
    print(fila)

print("*" * 45)
print("Modificar los Datos del Cliente")
id_modificar = input("Ingresa el Código del Cliente: ")
nueva_ciudad = input("Ingresa la nueva Ciudad del Cliente: ")

cursor.execute(
    "UPDATE clientes SET ciudad = %s WHERE id_clientes = %s",
    (nueva_ciudad, id_modificar)
)
conexion.commit()

print("-" * 45)
cursor.execute(
    "SELECT id_clientes, nombre, email, ciudad "
    "FROM public.clientes ORDER BY id_clientes"
)
print("Clientes en la base de datos")

for fila in cursor.fetchall():
    print(fila)


print("Datos Actualizados")
print("*" * 45)

cursor.close()
conexion.close()
print("Conexion cerrada")