# Clase en vídeo: https://youtu.be/_y9qQZXE24A

### Hola Mundo ###

# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

# Inicia el server: uvicorn main:app --reload  o con fastapy dev main.py   desde una consola term
# O bien para arrancar el server UVUCORN usando  fastapi dev main.py
# Detener el server: CTRL+C

# Para probar la APP se puede hacer instalando la extension THUNDER en VSCode

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

from fastapi import FastAPI
from routers import users_db

# Las siguientes instrucciones crearan una instancia de FastAPI
app = FastAPI()

# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=12475


# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=20480
app.include_router(users_db.router)

