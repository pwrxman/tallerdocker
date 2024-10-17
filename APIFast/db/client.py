
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

# Descomentar el db_client local o remoto correspondiente

# Base de datos local MongoDB
db_client = MongoClient()

# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=25470

# Base de datos remota MongoDB Atlas (https://mongodb.com)
# db_client = MongoClient(
#     "mongodb+srv://<user>:<password>@<url>/?retryWrites=true&w=majority").test

# Despliegue API en la nube:
# Deta - https://www.deta.sh/
# Intrucciones - https://fastapi.tiangolo.com/deployment/deta/