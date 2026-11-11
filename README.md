# Sistema de gestión de comercio – Python y PostgreSQL

## Datos del estudiante
- **Estudiante:** Miguel Ángel Salinas Fernández
- **Lenguaje:** Python 3
- **Base de datos:** PostgreSQL
- **Biblioteca:** psycopg2
- **Base de datos utilizada:** `comercio`

## Descripción
Este repositorio reúne ejercicios de Python conectados a una base de datos PostgreSQL. Los programas permiten consultar, insertar, modificar y eliminar registros de clientes, pedidos y productos.

## Archivos del proyecto

| Archivo | Función |
|---|---|
| `conexion.py` | Inserta varios clientes mediante `executemany`. |
| `Cliente.py` | Contiene una consulta de datos de clientes. Revisar el nombre de columna indicado en el SQL antes de ejecutarlo. |
| `ConsultarCliente.py` | Muestra los clientes registrados. |
| `ConsultarPedido.py` | Muestra pedidos junto con el nombre del cliente y del producto. |
| `BorrarCliente.py` | Muestra y permite eliminar un cliente por su identificador. |
| `BorrarPedido.py` | Muestra y permite eliminar un pedido por su identificador. |
| `BorrarProducto.py` | Muestra y permite eliminar un producto por su identificador. |

## Requisitos
- Python 3
- PostgreSQL
- Una base de datos llamada `comercio`
- Las tablas `clientes`, `pedidos` y `productos`, con las columnas utilizadas en las consultas
- La biblioteca `psycopg2`

## Instalación
Instalar la dependencia con:

```bash
pip install -r requirements.txt
```

## Configurar la conexión
Los programas usan estos datos de conexión:
- Host: `localhost`
- Puerto: `5432`
- Base de datos: `comercio`
- Usuario: `postgres`

Por seguridad, los archivos contienen `TU_CONTRASEÑA` como marcador y **no incluyen una contraseña real**. Antes de ejecutar un programa, reemplazá ese texto por la contraseña de tu propio servidor PostgreSQL. No publiques contraseñas en GitHub.

## Ejecutar los ejercicios
Desde una terminal abierta en la carpeta del proyecto, ejecutar el archivo que se desea probar. Por ejemplo:

```bash
python ConsultarCliente.py
```

También se pueden ejecutar los demás archivos:

```bash
python ConsultarPedido.py
python BorrarCliente.py
python BorrarPedido.py
python BorrarProducto.py
python conexion.py
python Cliente.py
```

**Atención:** estos programas realizan operaciones reales sobre la base de datos. Los archivos `Borrar*.py` eliminan registros y `conexion.py` inserta clientes. Probá primero con datos de prueba.

## Observaciones
- Los ejercicios dependen de que la base de datos y las tablas existan previamente.
- Los nombres de tablas y columnas deben coincidir con los de tu base de datos.
- `Cliente.py` contiene una consulta que usa `id_cliente` en el `ORDER BY`, mientras que otros ejercicios usan `id_clientes`. Verificá cuál es el nombre correcto en tu tabla antes de ejecutarlo.
- Este repositorio contiene los siete archivos recibidos; no se agregaron ejercicios que no fueron enviados.
