from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str
    nDocumento:int
    nombre:str
    telefono:int
    ciudad:str
    departamento:str
    direccion:str 
    
database_users = Dict[str, UserInDB]
database_users = {
"jessid22": UserInDB(**{"username":"jessid22",
                        "password":"lider",
                        "nDocumento":"1030569305",
                        "nombre":"Jessid Escobar",
                        "telefono":"3118023190",
                        "ciudad":"bogotá",
                        "departamento":"bogotá",
                        "direccion":"av siempre viva 123"
                        }),
"emmanuel35": UserInDB(**{"username":"emmanuel35",
                        "password":"sensey",
                        "nDocumento":"1030569305",
                        "nombre":"Emmanuell Garnica",
                        "telefono":"3118023195",
                        "ciudad":"Madrid",
                        "departamento":"Cundinamarca",
                        "direccion":"av siempre viva 124"                        
                        }),
"nohora123": UserInDB(**{"username":"nohora123",
                        "password":"lider2",
                        "nDocumento":"1030569307",
                        "nombre":"Nohora España",
                        "telefono":"3118023194",
                        "ciudad":"Madrid",
                        "departamento":"Cundinamarca",
                        "direccion":"av siempre viva 127"                        
                        }),
"janeth123": UserInDB(**{"username":"janeth123",
                        "password":"lider3",
                        "nDocumento":"1030569399",
                        "nombre":"Janeth Fernandez",
                        "telefono":"3118023199",
                        "ciudad":"Soacha",
                        "departamento":"Cundinamarca",
                        "direccion":"av siempre viva 365"                        
                        }),                        
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    print(database_users[user_in_db.username])
    



