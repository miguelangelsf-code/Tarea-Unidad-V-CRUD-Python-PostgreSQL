# Trabajo práctico – Gestión de comercio con Python y PostgreSQL

**Asignatura:** Optativo I – Python  
**Tema:** Conexión a bases de datos y operaciones CRUD  
**Alumno/a:** Completar con tu nombre

## Descripción

Este repositorio contiene programas de Python que se conectan a una base de datos **PostgreSQL** llamada `comercio`.
Permiten registrar, consultar, modificar y eliminar **clientes, productos y pedidos** mediante instrucciones SQL.
Cada programa puede ejecutarse por separado desde la terminal.

> A diferencia del repositorio usado como referencia (ejercicios de POO), este trabajo se centra en operaciones CRUD y relaciones entre tablas.

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

## Cómo preparar el proyecto

**1. Crear la base de datos.** En pgAdmin o en `psql`, crear una base llamada `comercio`:

```sql
CREATE DATABASE comercio;
```

Seleccionar esa base y ejecutar el contenido de `sql/esquema.sql`. También se puede usar desde la terminal:

```bash
psql -U postgres -d comercio -f sql/esquema.sql
```

> Si las tablas ya existen, el script `IF NOT EXISTS` no cambia su estructura. Comprueba que las columnas coincidan antes de ejecutar los programas.

**2. Instalar las bibliotecas.** Abrir la terminal en la carpeta del proyecto y ejecutar:

```bash
python -m pip install -r requirements.txt
```

**3. Configurar la conexión.** Hacer una copia de `.env.example` y llamarla `.env`.
Completar `DB_PASSWORD` con la contraseña **de tu propia instalación de PostgreSQL**.
El archivo `.env` queda en tu computadora y **no debe publicarse**.

**4. Probar la conexión.**

```bash
python conexion.py
```

## Cómo ejecutar los programas

Para registrar datos por primera vez, ejecutar en este orden:

```bash
python Cliente.py
python Producto.py
python Pedido.py
```

Para consultar y modificar los datos:

```bash
python ConsultarCliente.py
python ConsultarProducto.py
python ConsultarPedido.py
```

Para borrar registros:

```bash
python BorrarPedido.py
python BorrarCliente.py
python BorrarProducto.py
```

Algunos programas solicitan un código o un valor por teclado. Los archivos de registro agregan nuevos datos **cada vez que se ejecutan**; no son una carga única automática.

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

## Observaciones

Los tres archivos `Consultar...py` **también modifican** datos, tal como lo hacían los programas originales. Se normalizó el nombre `ConsultarProducto(1).py` a `ConsultarProducto.py`.

No se incluye una base de datos real ni una contraseña. Para comprobar la ejecución completa es necesario tener PostgreSQL disponible localmente.
