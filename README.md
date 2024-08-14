# Sistema de Distribución de Escaños usando el Método D'Hondt

Este proyecto implementa una API RESTful para calcular la distribución de escaños utilizando el método D'Hondt, desarrollado con Python 3.11, FastAPI, SQLAlchemy y Pydantic.

## Requisitos

- Docker
- Docker Compose

## Estructura del Proyecto

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   └── routers
│       ├── __init__.py
│       └── escaños.py
├── alembic.ini
├── alembic
│   ├── env.py
│   └── versions
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Configuración de la Base de Datos

El proyecto utiliza PostgreSQL como sistema de gestión de bases de datos. La configuración se encuentra en el archivo `docker-compose.yml`.

## Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd <nombre-del-directorio>
```

### 2. Ejecutar la aplicación usando Docker Compose

Este comando levantará tanto la base de datos como la API.

```bash
docker-compose up --build
```

### 3. Acceder a la API

Una vez que el contenedor esté en funcionamiento, puedes acceder a la API en la siguiente URL:

```
http://localhost:8000
```

### 4. Acceder a la Documentación de la API

La documentación generada automáticamente por FastAPI está disponible en:

```
http://localhost:8000/docs
```

### 5. Migraciones de Base de Datos

Si necesitas aplicar migraciones en la base de datos, puedes acceder al contenedor de la API y ejecutar los comandos de Alembic:

```bash
docker-compose exec api bash
alembic upgrade head
```

## Endpoints

### 1. Calcular Distribución de Escaños

- **Ruta**: `/calcular`
- **Método**: `POST`
- **Descripción**: Realiza el cálculo de distribución de escaños utilizando el método D'Hondt y almacena el resultado.
- **Cuerpo**:

```json
{
  "escaños": 10,
  "votos": {
    "Lista A": 1000,
    "Lista B": 800,
    "Lista C": 600
  }
}
```

### 2. Consultar Historial de Cálculos

- **Ruta**: `/historial`
- **Método**: `GET`
- **Descripción**: Retorna el historial de cálculos realizados.
- **Parámetros**:
  - `skip`: Desplazamiento para paginación.
  - `limit`: Límite de registros a retornar.

### 3. Consultar Cálculo Específico

- **Ruta**: `/calculo/{calculo_id}`
- **Método**: `GET`
- **Descripción**: Consulta un cálculo específico por su ID.
- **Respuesta**: Devuelve el número de escaños, los votos originales y la distribución de escaños para cada lista.

### Notas Adicionales

- El archivo `docker-compose.yml` define dos servicios: `db` para la base de datos PostgreSQL y `api` para la aplicación FastAPI.
- El volumen `postgres_data` se utiliza para persistir los datos de la base de datos.
- Asegúrate de ajustar `DATABASE_URL` en caso de que cambies las credenciales o el nombre de la base de datos.
