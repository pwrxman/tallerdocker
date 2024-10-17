
# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=20480)

### MongoDB client ###

# Descarga versión community: https://www.mongodb.com/try/download/community
# Instalación:  https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/

# Para este ejercicio se utilizará  MongoDB 7.0 Community Edition supports macOS 11 or later

# To start mongodb/brew/mongodb-community now and restart at login:
# brew services start mongodb/brew/mongodb-community
# To stop a mongod running as a macOS service, use the following command as needed:
# brew services stop mongodb-community@7.0

# Se crean los sioguientes archivos / directorios
# '/usr/local/Homebrew/Library/Taps/homebrew/homebrew-services'
# configuration file  ->  /opt/homebrew/etc/mongod.conf
# log directory       ->  /opt/homebrew/var/log/mongodb
# data directory      ->  /opt/homebrew/var/mongodb

# To begin using MongoDB, connect mongosh to the running instance. From a new terminal, issue the following:
# mongosh

# Instalar en VSCode la extension de "MongoDB for VS Code"
# Utilizando la extension, para conectar con la DB escriba "mongodb://localhost"

# Módulo conexión MongoDB: pip install pymongo
# Ejecución: sudo mongod --dbpath "/path/a/la/base/de/datos/"
# Conexión: mongodb://localhost

from pymongo import MongoClient
import certifi

# Descomentar el db_client local o remoto correspondiente

# USANDO UNA BASE DE DATOS LOCAL DE MongoDB en 127.0.0.1
# db_client = MongoClient().local

# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=25470

# USANDO UNA BASE DE DATOS REMOTA DE MongoDB Atlas (https://mongodb.com)
    # Hacer login en mongoDB
    # Crear un nuevo Proyecto
    # Project:  Curso Python BraisMoure
    # Databasename: Cluster0
    # My IP Address: 201.141.16.166
    # crear un usuario y password para la BD -> user DB: amatest   pwd: Kanito24

    # Para conectarse desde VS Code use:  
    # In VS Code, open the Command Palette.
    # Click on "View" and open "Command Palette."
    # Search "MongoDB: Connect" on the Command Palette and click on "Connect with Connection String."
    # Use el siguiente string:
    # mongodb+srv://amatest:LaChiquis15@cluster0.9pcaq.mongodb.net/

    # Para conectarse desde la aplicacion use:
    # Connecting with MongoDB Driver
    # 1. Select your driver and version.   En este caso utilizaremos PYTHON
    # 2. Install your driver running the following on the command line
        # Note: Use appropriate Python 3 executable
        # python -m pip install "pymongo[srv]"
    # 3. Add your next connection string into your application code  proporcionado por MongoDB
        # uri = "mongodb+srv://amatest:Kanito24@cluster0.9pcaq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # 4. En mi caso hay que importar la libreria  "certifi" para evitar un error de certificados
    #    Entonces añadir en la linea de conexion el parametro  "tlsCAFile=certifi.where()"
# Entonces la cadena de conexion queda como sigue (al final se pone test porque es la base de datos por defecto al a que se conecta)
# db_client = MongoClient("mongodb+srv://amatest:LaChiquis15@cluster0.9pcaq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").test
uri = "mongodb+srv://amatest:Kanito24@cluster01.9pcaq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster01"
# Create a new client and connect to the server
db_client = MongoClient(uri, tlsCAFile=certifi.where()).test


"""
# CODIGO EJEMPLO para probar que la BD contesta
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
uri = "mongodb+srv://amatest:Kanito24@cluster01.9pcaq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster01"
# Create a new client and connect to the server
# db_client = MongoClient(uri, server_api=ServerApi('1'))
db_client = MongoClient(uri, tlsCAFile=certifi.where()).test
# Send a ping to confirm a successful connection
try:
    db_client.command('ping')
    print("PINGED YOUR DEPLOYMENT. You successfully connected to MongoDB!")
except Exception as e:
    print("ERRORRRRR  NO SE CONECTO A MONGO {}".format(e))
finally:
    print("CONEXION FINALIZADA")    


# Despliegue API en la nube:
# Deta - https://www.deta.sh/
# Intrucciones - https://fastapi.tiangolo.com/deployment/deta/

"""