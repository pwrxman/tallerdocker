# JWT  JSON WEB TOKEN

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "994bc41d4f21b7475774f0e085325314b084e3170016fbda7e01b69b14b07f7f"  # generado con el comando "openssl rand -hex 32"

router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool
    
class UserDB(User):
    password: str

# Los passwords fueron encriptados utilizando https://www.browserling.com/tools/bcrypt
# los passwords originales fueron 123456, 789012 y 345678 respectivamente para cada uno de los usuarios utilizados
users_db = {
    "mouredev": {"username": "mouredev", "full_name": "Moure", "email": "moure@mail.com", "disabled": False, "password": "$2a$10$HTNLtutu5qumsXtvL0Rptu77q6AmGKEjBNf8JlkLpB7xBAGj1bAza"},
    "jastaton": {"username": "jastaton", "full_name": "Jason Staton", "email": "jstaton@kail.com", "disabled": False, "password": "$2a$10$LJIec2iVayThlG9.kNtVm.Bb42zAnkbY7Y2jZ3ICAEUeHLIBEF686"},
    "sistalon": {"username": "sistalon", "full_name": "Silvester Stallone", "email": "stalon@haakon.com", "disabled": True, "password": "$2a$10$GSCBRejwCnIcXoCPs4yZfu2foQHZeBbNRuI102HBq73pKfex15Tzy"}
            }

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])   # INVESTIGAR QUE CHINGADOS SIGNIFICAN LOS DOS ASTERISCOS, TIENE AL>GO QUE VER CON EL BaseModel

def search_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])   # INVESTIGAR QUE CHINGADOS SIGNIFICAN LOS DOS ASTERISCOS, TIENE AL>GO QUE VER CON EL BaseModel


async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , 
                            detail="Credenciales de autenticación inváidas", 
                            headers={"www-Authenticate": "Bearer"})

    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception


    except InvalidTokenError:
        raise exception
    
    return search_user(username)

# Criterio de dependencia
async def current_user(user: User = Depends(auth_user)):  
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST , 
                            detail="Usuario Inactivo")
    return user


@router.post("/login") 
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no Es Correcto")
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El password no Es Correcto")
    
    access_token = {"sub": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM) , "token_type": "bearer"} # el token generado puede ser validado en jwt.io



@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
