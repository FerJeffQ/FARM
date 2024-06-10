# FARM
Project about FastAPI React MongoDb

### Base de datos
```
docker-compose up -d
```
### Creando BackEnd
```
mkdir backend
cd backend
python -m venv venv
```
Activar el entorno
```
 # In cmd.exe
 venv\Scripts\activate.bat
 # In PowerShell
 venv\Scripts\Activate.ps1
 # Linux
 source myvenv/bin/activate
```
Instalacion de dependencias
```
pip install fastapi motor
```
Estructura del Proyecto
```
├── app
│   ├── __init__.py
│   ├── main.py
│   └── server
│       ├── app.py
│       ├── database.py
│       ├── models
│       │   └── task.py
│       └── routes
│           └── task.py
├── .env
└── requirements.txt
```
```
app: Este es el directorio raíz de tu aplicación.

__init__.py: Este archivo se utiliza para indicar a Python que este directorio debe ser tratado como un paquete.

main.py: Este es el punto de entrada de tu aplicación. Aquí es donde FastAPI se inicializa y se ejecuta.

server: Este directorio contiene los detalles específicos de tu aplicación.

app.py: Este archivo se utiliza para crear y configurar la aplicación FastAPI.

database.py: Este archivo se utiliza para manejar la conexión a tu base de datos MongoDB.

models: Este directorio se utiliza para definir los modelos de tus datos.

routes: Este directorio se utiliza para definir las rutas de tu aplicación.

requirements.txt: Este archivo lista todas las dependencias de Python que tu proyecto necesita.
```
Ejecutar desde Backend:
```
uvicorn app.main:app --reload
```
Ejecutar el servidor:
```
uvicorn app.main:app --reload
```