# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=5382

### Users API ###

from fastapi import APIRouter

router = APIRouter(prefix="/products", 
                   tags=["products"],
                   responses={404: {"message": "No Encontrado"}})

products_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

# Utilizando la Entidad products
@router.get("/")    # como en la declaracion de router ya se tiene el prefix="/productos", ya no es necedsario ponerlo aqui
async def products():
    return ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]


@router.get("/{id}")    # como en la declaracion de router ya se tiene el prefix="/productos", ya no es necedsario ponerlo aqui
async def products(id: int):
    return products_list[id]
