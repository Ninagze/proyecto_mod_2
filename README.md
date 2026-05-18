# Análisis de Datos de Spotify y Dashboard Interactivo

Este proyecto realiza un análisis exploratorio de datos (EDA) sobre un conjunto de datos de canciones de Spotify. El proceso incluye la ingesta, limpieza y transformación de los datos, cargándolos en una base de datos SQL para un análisis robusto. Finalmente, los hallazgos se presentan en un dashboard interactivo construido con Streamlit.

## 🚀 Características

- **Pipeline de Datos ETL**: Proceso completo de Extracción, Transformación y Carga de datos desde archivos CSV a una base de datos MySQL/TiDB.
- **Limpieza de Datos**: Tratamiento de valores nulos, duplicados y transformación de tipos de datos para asegurar la calidad del análisis.
- **Análisis Exploratorio de Datos (EDA)**: Investigación de las relaciones entre características de las canciones como popularidad, bailabilidad, energía y valencia.
- **Dashboard Interactivo**: Una aplicación web creada con Streamlit que permite visualizar los resultados del análisis a través de métricas y gráficos interactivos.
- **Persistencia en Base de Datos**: Uso de SQLAlchemy para gestionar la conexión y la carga de datos en una base de datos relacional.

## 📂 Estructura del Proyecto

```
proyecto_mod_2/
│
├── data/
│   ├── artists.csv         # Datos brutos de artistas (ignorado por Git)
│   └── tracks.csv          # Datos brutos de canciones (ignorado por Git)
│
├── exports/
│   └── analytical_dataset.csv # Dataset limpio y procesado, listo para el análisis
│
├── notebooks/
│   └── proyecto_final.ipynb  # Notebook principal con todo el proceso de ETL y EDA
│
├── sql/
│   └── create_tables.sql   # Script SQL para la creación de las tablas en la BD
│
├── streamlit_app/
│   └── app.py              # Código de la aplicación del dashboard con Streamlit
│
├── .gitignore              # Archivos y carpetas ignorados por Git
├── requirements.txt        # Dependencias de Python para el proyecto
└── README.md               # Este archivo
```

## 🛠️ Configuración del Entorno

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

### 1. Prerrequisitos

- Python 3.8 o superior
- Git
- Acceso a una base de datos MySQL o compatible ( TiDB Cloud)

### 2. Clonar el Repositorio

```bash
git clone https://github.com/Ninagze/proyecto_mod_2.git
cd proyecto_mod_2
```

### 3. Instalar Dependencias

Se recomienda crear un entorno virtual para aislar las dependencias del proyecto.

```bash
# Crear un entorno virtual (opcional pero recomendado)
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar las librerías necesarias
pip install -r requirements.txt
```

### 4. Configurar la Base de Datos

El notebook `proyecto_final.ipynb` requiere una URL de conexión para acceder a la base de datos. Deberás crear las tablas y configurar la conexión.

1.  **Crear la Base de Datos**: Asegúrate de tener una base de datos creada (por ejemplo, `spotify_db`).

2.  **Crear las tablas**: Ejecuta el siguiente código SQL en tu cliente de base de datos preferido para crear las tablas `artists` y `tracks`. El script completo también se encuentra en `sql/create_tables.sql`.

    ```sql
    CREATE TABLE artists (
        artist_id VARCHAR(250) PRIMARY KEY,
        artist_name VARCHAR(255),
        genres TEXT,
        followers INT,
        popularity INT
    );

    CREATE TABLE tracks (
        track_id VARCHAR(250) PRIMARY KEY,
        track_name VARCHAR(255),
        artist_id VARCHAR(250),
        release_year INT,
        popularity INT,
        danceability FLOAT,
        energy FLOAT,
        valence FLOAT,
        acousticness FLOAT,
        instrumentalness FLOAT,
        liveness FLOAT,
        speechiness FLOAT,
        tempo FLOAT,
        duration_ms INT,
        time_signature INT,
        FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
    );
    ```

3.  **Establecer la URL de conexión**: Modifica la celda correspondiente en el notebook (`notebooks/proyecto_final.ipynb`) con tu URL de conexión a la base de datos. El formato es:
    ```python
    # Ejemplo de URL para MySQL con PyMySQL
    DATABASE_URL = "mysql+pymysql://<usuario>:<contraseña>@<host>:<puerto>/<nombre_bd>"
    ```

## 📈 Uso

### 1. Ejecutar el Notebook de Análisis

Para procesar los datos y generar el archivo `analytical_dataset.csv`, debes ejecutar todas las celdas del notebook `notebooks/proyecto_final.ipynb`.

1.  Abre el proyecto en VS Code o inicia Jupyter Lab.
2.  Navega y abre el archivo `notebooks/proyecto_final.ipynb`.
3.  Ejecuta todas las celdas en orden. Esto poblará tu base de datos y creará el archivo en la carpeta `exports/`.

### 2. Lanzar el Dashboard de Streamlit

Una vez que el archivo `analytical_dataset.csv` ha sido generado, puedes iniciar la aplicación interactiva.

```bash
streamlit run streamlit_app/app.py
```

Esto abrirá una nueva pestaña en tu navegador con el dashboard interactivo.

## 💻 Tecnologías Utilizadas

- **Lenguaje**: Python
- **Análisis de Datos**: Pandas, NumPy
- **Base de Datos**: SQLAlchemy, PyMySQL (para conexión a MySQL/TiDB)
- **Visualización**: Matplotlib, Seaborn, Plotly Express
- **Dashboard**: Streamlit
- **Control de Versiones**: Git y GitHub
