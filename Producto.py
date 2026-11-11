
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

productos_nuevos = [
    ("Monitor AOC 27G4E de 27 Full HD 180Hz 0.5 ms con DisplayPort HDMI", 1500000, 15),
    ("Teclado Gaming Mecánico Satellite GK-501 Portugués USB - Negro", 200000, 20),
    ("Mouse Gaming Logitech G203 USB hasta 8.000 DPI con Backlight RGB - Púrpura", 130000, 10),
    ("Soporte para Notebook Satellite A-CP20 con 2 USB y Cooler de 140 mm - Negro",60000, 8),

]

cursor.executemany(
    'INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)',
    productos_nuevos
)
conexion.commit()

print(f"{cursor.rowcount} productos insertados de una sola vez")
print("-" * 45)

cursor.close()
conexion.close()
print("Conexion cerrada")

