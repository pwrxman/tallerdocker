
### Users MongoDB API ###

from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId


# router = APIRouter()

# Tambien se podria utilizar la siguiente definicion para simplificar la definicion de los router
router = APIRouter(prefix="/userdb", 
                    tags=["userdb"],
                    responses={status.HTTP_404_NOT_FOUND : {"message": "No Encontrado"}})


#  AHORA PONGAMOS UN POST
#  para INSERTAR y/o crear un nuevo usuario

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)  # Respuest por defecto cuando OK ; Codigo de respuesta por defecto
async def user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="El Usuario ya existe usando HTTPEXCEPTION")  # Codigo especifico por el error ocurrido

    user_dict = dict(user) 
    del user_dict["id"]   

    id = db_client.users.insert_one(user_dict).inserted_id

    # _id es el nombre por defecto del campo donde MongoDB almcena el ID único
    new_user = user_schema(db_client.users.find_one({"_id": id}))

    return User(**new_user)


# Para hacer una consulta a la base de datos
@router.get("/list", response_model=list[User])  # Obtener un listado de usuarios en la DB  GET 127.0.0.1:8000/userdb
async def users():
    return users_schema(db_client.users.find())

# Consulta por PATH
@router.get("/{id}")  # Path   # Buscar un usuario especifico por ID  GET 127.0.0.1:8000/userdb/66c0400c997b66ca7504ce29 donde la clave es el ID del usuario
async def user(id: str):
    return search_user("_id", ObjectId(id))

# Consulta por QUERY
@router.get("/user/")  # Query  # Buscar por QUERY  GET 127.0.0.1:8000/userdb/user/?id=66c0400c997b66ca7504ce29 donde la clave es el ID del usuario
async def user(id: str):
    return search_user("_id", ObjectId(id))

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)  # DELETE 127.0.0.1:8000/userdb/66c0400c997b66ca7504ce29 donde la clave es el ID del usuario
async def user(id: str):
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error": "No se ha eliminado el usuario"}



# Actualizar un usuario UPDATE
@router.put("/", response_model=User)  # PUT 127.0.0.1:8000/userdb e incluir el JSON completo en la peticion
async def user(user: User):

    user_dict = dict(user)
    del user_dict["id"]

    try:
        # el replace cambia el registro completo, el update solo actualiza el campo deseado
        db_client.users.find_one_and_replace(
            {"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"error": "No se ha actualizado el usuario"}

    return search_user("_id", ObjectId(user.id))

def search_user(field: str, key):
    try:
        user = db_client.users.find_one({field: key})
        return User(**user_schema(user))

    except:
        return {"error": "No se ha encontrado el usuario por funcion"}



