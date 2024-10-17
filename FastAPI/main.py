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
from routers import products, users, basic_auth_users_routers, jwt_auth_users_routers, users_db
from fastapi.staticfiles import StaticFiles

# Las siguientes instrucciones crearan una instancia de FastAPI
app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)     # @router.get("/usersjson")

app.include_router(basic_auth_users_routers.router)
app.include_router(jwt_auth_users_routers.router)
app.include_router(users_db.router)

app.mount("/static", StaticFiles(directory="static"), name="static")


# @router.get("/usersjson")
# @router.get("/usersclass")
# @router.get("/userslist")
# @router.get("/user1list")
# @router.get("/userp/{id}")
# @router.get("/userq/")
# @router.get("/user_f_path/{id}")
# @router.get("/user_f_path/")
# @router.post("/userpost/")
# @router.post("/userposthe/"
# @router.put("/userput/")
# @router.delete("/userdel/{id}", )


@app.get("/")
async def root():
    return "Hello World FastAPI Again"

@app.get("/url")
async def url():
    return {"URL del Curso": "https://mouredev.com/python"}

"""
# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=12475
app.include_router(products.router)
app.include_router(users.router)

# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=14094
app.include_router(basic_auth_users.router)

# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=17664
app.include_router(jwt_auth_users.router)

# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=20480
app.include_router(users_db.router)

# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=13618
app.mount("/static", StaticFiles(directory="static"), name="static")


# Url local: http://127.0.0.1:8000


@app.get("/")
async def root():
    return "Hola FastAPI!"

# Url local: http://127.0.0.1:8000/url


@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}


    
    If you are curious about how the raw OpenAPI schema looks like, 
    FastAPI automatically generates a JSON (schema) with the descriptions of all your API.

    You can see it directly at: http://127.0.0.1:8000/openapi.json.

    {
  "openapi": "3.1.0",
  "info": {
    "title": "FastAPI",
    "version": "0.1.0"
  },
  "paths": {
    "/": {
      "get": {
        "summary": "Root",
        "operationId": "root__get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        }
      }
    },
    "/url": {
      "get": {
        "summary": "Url",
        "operationId": "url_url_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        }
      }
    }
  }
}

"""