from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool
    
class UserDB(User):
    password: str

users_db = {
    "mouredev": {"username": "mouredev", "full_name": "Moure", "email": "moure@mail.com", "disabled": False, "password": "123456"},
    "jastaton": {"username": "jastaton", "full_name": "Jason Staton", "email": "jstaton@kail.com", "disabled": False, "password": "780123"},
    "sistalon": {"username": "sistalon", "full_name": "Silvester Stallone", "email": "stalon@haakon.com", "disabled": True, "password": "456789"}
            }

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])   # INVESTIGAR QUE CHINGADOS SIGNIFICAN LOS DOS ASTERISCOS, TIENE AL>GO QUE VER CON EL BaseModel

def search_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])   # INVESTIGAR QUE CHINGADOS SIGNIFICAN LOS DOS ASTERISCOS, TIENE AL>GO QUE VER CON EL BaseModel


# Criterio de dependencia
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , 
                            detail="Credenciales de autenticación inváidas", 
                            headers={"www-Authenticate": "Bearer"})
    
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST , 
                            detail="Usuario Inactivo")

    
@app.post("/login") 
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no Es Correcto")
    
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El password no Es Correcto")
    
    return {"access_token": user.username , "token_type": "bearer"} 

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user



