import psycopg2

conexion = psycopg2.connect (
    host='localhost',
    port=5432,
    dbname='comercio',
    user='postgres',
    password='******'
)

print('Conexion exitosa a la base de datos')

cursor = conexion.cursor()

cursor.execute('SELECT id_clientes, nombre, email, ciudad, fecha_alta FROM public.clientes ORDER BY id_cliente')


conexion.commit()
print('Cliente insertado correctamente')