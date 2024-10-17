from pydantic import BaseModel

class User(BaseModel):
    id: str | None = None   # MongoDB Asigna un ID de tipo str por defecto, entonces al insertar un nuevo registro puede que nos llegue vacio 
    username: str
    email: str
    
