# Trabajo práctico – Gestión de comercio con Python y PostgreSQL

**Asignatura:** Optativo I – Python  
**Tema:** Conexión a bases de datos y operaciones CRUD  
**Alumno/a:** Miguel Ángel Salinas Fernández

## Descripción

Este repositorio contiene programas de Python que se conectan a una base de datos **PostgreSQL** llamada `comercio`.
Permiten registrar, consultar, modificar y eliminar **clientes, productos y pedidos** mediante instrucciones SQL.
Cada programa puede ejecutarse por separado desde la terminal.

## Archivos del proyecto

| Archivo | Función |
| --- | --- |
| `conexion.py` | Crea y comprueba la conexión a PostgreSQL usando `.env`. |
| `Cliente.py` | Inserta cuatro clientes de ejemplo. |
| `Producto.py` | Inserta cuatro productos de ejemplo. |
| `Pedido.py` | Inserta cuatro pedidos y muestra sus datos relacionados. |
| `ConsultarCliente.py` | Muestra los clientes y permite cambiar la ciudad de uno. |
| `ConsultarProducto.py` | Muestra los productos y permite cambiar el precio de uno. |
| `ConsultarPedido.py` | Muestra los pedidos y permite cambiar la cantidad de uno. |
| `BorrarCliente.py` | Elimina un cliente por su código. |
| `BorrarProducto.py` | Elimina un producto por su código. |
| `BorrarPedido.py` | Elimina un pedido por su código. |
| `sql/esquema.sql` | Crea las tablas `clientes`, `productos` y `pedidos`. |
| `requirements.txt` | Lista las bibliotecas necesarias. |
| `.env.example` | Modelo de configuración de la base de datos, sin contraseña. |
| `.gitignore` | Evita subir contraseñas y archivos temporales a GitHub. |

## Requisitos

- Python 3.10 o posterior.
- PostgreSQL instalado y funcionando (por ejemplo, desde pgAdmin).
- Acceso a una base de datos llamada `comercio`.


## Tablas y relaciones

- **clientes:** código, nombre, correo, ciudad y fecha de alta.
- **productos:** código, nombre, precio y stock.
- **pedidos:** código, cliente, producto, cantidad y fecha.

Los pedidos se relacionan con clientes y productos mediante claves foráneas. Por eso, un cliente o producto que tenga pedidos asociados no se puede borrar directamente: primero se deben eliminar esos pedidos.

## Conceptos utilizados

- Conexión Python a PostgreSQL con `psycopg2`.
- Consultas `SELECT`, `INSERT`, `UPDATE` y `DELETE`.
- Relaciones de tablas mediante `INNER JOIN`.
- Consultas parametrizadas (`%s`) y `executemany()`.
- Validación básica de datos introducidos por teclado.
- Confirmación (`commit`) y reversión (`rollback`) automáticas mediante el administrador de contexto de la conexión.
- Variables de entorno para mantener privadas las credenciales.
