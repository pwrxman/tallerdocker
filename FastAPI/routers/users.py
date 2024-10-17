# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=5382

### Users API ###

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

#  Entidad USER
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_list = [User(name = "Brais", surname = "Moure", url = "https://moure.dev", age = 35),
              User(name = "Moure", surname = "Dev", url = "https://mouredev.com", age = 35),
              User(name = "Haakon", surname = "Dahlberg", url = "https://haakon.com", age = 64)]

# Construir el JASON a mano    NO ES LO HABITUIAL O NORMAL!!
@router.get("/usersjson")
async def usersjson():
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
            {"name": "Moure", "surname": "Dev", "url": "https://mouredev.com", "age": 35},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com", "age": 33}]

# Construir el JSON Automaticamente
@router.get("/usersclass")
async def usersclas():
    return User(name = "Brais", surname = "Moure", url = "https://moure.dev", age = 53)
    

# Pasando Parametros en el PATH
class User1(BaseModel):
    id: int 
    name: str
    surname: str
    url: str
    age: int

users1_list = [User1(id=1, name="Brais", surname="Moure",    url="https://moure.dev",    age=35),
               User1(id=2, name="Moure", surname="Dev",      url="https://mouredev.com", age=35),
               User1(id=3, name="Brais", surname="Dahlberg", url="https://haakon.com",   age=54)]  

@router.get("/user1list")
async def userslist():
    return users1_list   

@router.get("/userp/{id}")
async def userpa(id: int):
    usersp = filter(lambda user1: user1.id == id, users1_list)
    try:
        return list(usersp)[0]
    except:
        return {"ERRORP": "ID de usuario por PATH no encontrado!"}

# Pasando Parametros en el QUERY
# la momento de invocar la página se debra pasar el parámetro de la siguiente manera
# http://127.0.0.1:8000/userquery/?id=x  donde x el id del usuario buscado

@router.get("/userq/")
async def userpa(id: int):
    usersp = filter(lambda user1: user1.id == id, users1_list)
    try:
        return list(usersp)[0]
    except:
        return {"ERRORQ": "ID de usuario por QUERY no encontrado!"}


# Optimizando las operaciones a traves del uso de una funcion

@router.get("/user_f_path/{id}")
async def users(id: int):
    return search_user(id)

@router.get("/user_f_path/")
async def users(id: int):
    return search_user(id)


#  AHORA PONGAMOS UN POST
#  para insertar y/o crear un nuevo usuario
@router.post("/userpost/")
async def user(user: User1):
    if type(search_user(user.id)) == User1:
        return {"error": "El Usuario ya existe"}
    
    users1_list.append(user)
    return user

#  AHORA HAGAMOS UN POST UTILIZANDO HttpException
#  para insertar y/o crear un nuevo usuario
@router.post("/userposthe/", response_model=User1, status_code=201)  # Respuest por defecto cuando OK ; Codigo de respuesta por defecto
async def user(user: User1):
    if type(search_user(user.id)) == User1:
        raise HTTPException(status_code=404, detail="El Usuario ya existe usando HTTPEXCEPTION")  # Codigo especifico por el error ocurrido
        
    users1_list.append(user)
    return user



#  AHORA PONGAMOS UN PUT
#  para actualizar un usuario
@router.put("/userput/")
async def user(user: User1):
    found = False
    for  index, saved_user in enumerate(users1_list):
        if saved_user.id == user.id:
            users1_list[index] = user
            found = True
            
    if not found:
        return {"error": "El Usuario NO se actualizò"}
    
    return user

#  AHORA HAGAMOS UN DELETE
#  para eliminar un usuario
@router.delete("/userdel/{id}", )
async def user(id: int):
    found = False
    for  index, saved_user in enumerate(users1_list):
        if saved_user.id == id:
            del users1_list[index]
            found = True
    if not found:
        return {"error": "El Usuario NO se encontró para borrarlo"}        

def search_user(id: int):
    users2 = filter(lambda user: user.id == id, users1_list)
    try:
        return list(users2)[0]
    except:
        return {"error": "No se ha encontrado el usuario por funcion"}







"""

router = APIRouter()

#  Entidad USER
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
              User(id=2, name="Moure", surname="Dev",
                   url="https://mouredev.com", age=35),
              User(id=3, name="Brais", surname="Dahlberg", url="https://haakon.com", age=33)]


@router.get("/usersjson")
async def usersjson():  # Creamos un JSON a mano
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
            {"name": "Moure", "surname": "Dev",
                "url": "https://mouredev.com", "age": 35},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com", "age": 33}]


@router.get("/users")
async def users():
    return users_list


@router.get("/user/{id}")  # Path
async def user(id: int):
    return search_user(id)


@router.get("/user/")  # Query
async def user(id: int):
    return search_user(id)


# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=8529


@router.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")

    users_list.append(user)
    return user


@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}

    return user


@router.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usuario"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}


""" 