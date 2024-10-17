from fastapi import FastAPI
from databases import Database
import sclalchemy
from handlers import users_handler
from schemas.user import UserCreate,UserUpdate, UserAuthorize
from database import metadata, engine, database
from models import users
from models.Users import UserRole

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()   

@app.get("/users/")
async def read_users():
    query = users.select()
    return await database.fetch_all(query)    

@app.post("/users/")
async def creat_users(name: str, email: str):
        return await users_handler.read_users(database,role)

@app.post("/users/")
async def create_user(user: UserCreate, role: UserRole):
    return await users_handler.create_user(user,database)

@app.delete("/users/")
async def delete_user(email: str):
    return await users_handler.delete_user(email, database)

@app.put("/users/")
async def update_user(user: UserUpdate):
   return await users_handler.update_user(user, database)
@app.put("/users/authorize/")
async def authorize_user(user: UserAuthorize):
    return await users_handler.authorize_user(user, database)