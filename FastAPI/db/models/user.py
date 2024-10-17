
# PARA VERSIONES DE PYTHON MENORES A 3.9 USE LO SIGUIENTE
# from pydantic import BaseModel

# class User(BaseModel):
#     id: str | None = None   # MongoDB Asigna un ID de tipo str por defecto, entonces al insertar un nuevo registro puede que nos llegue vacio 
#     username: str
#     email: str

# PARA VERSIONES DE PYTHON SUPERIORES A 3.9 USE LO SIGUIENTE
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[str]   # MongoDB Asigna un ID de tipo str por defecto, entonces al insertar un nuevo registro puede que nos llegue vacio 
    username: str
    email: str

