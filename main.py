import uvicorn
from fastapi import FastAPI
from fastapi import HTTPException
from db.user_db import UserInDB
from db.user_db import get_user,update_user
from models.user_models import UserIn,UserOut,User,Mensaje

api =FastAPI()

from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080","http://localhost:8080/perfil",
    "http://127.0.0.1:8080", "http://127.0.0.1:8080/perfil","https://cinsell.herokuapp.com/crear",
    "https://cinsell.herokuapp.com/users","https://cinsell.herokuapp.com/login"
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)
@api.post("/login/")
async def users_post(user_in:UserIn):
    user = get_user(user_in.username)
    if user == None:
        raise HTTPException(status_code=404,
    detail="El usuario no existe")
    if user.password != user_in.password:
            return {"Autenticado": False}
    return {"Autenticado": True}

@api.post("/crear/")
async def users_put(user_in:UserOut):
    user = get_user(user_in.username)
    if user != None:
         raise HTTPException(status_code=404,
    detail=False)
    update_user(user_in)     
    raise HTTPException(status_code=200,
    detail=True)  

@api.get("/users/{user}")
async def users_get(user:str):
    user = get_user(user)
    if user == None:
        raise HTTPException(status_code=404,
    detail="El usuario no existe")
    user_out = UserOut(**user.dict())
    return user_out
