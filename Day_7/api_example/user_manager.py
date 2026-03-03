from fastapi import FastAPI, Response, status
from userdb import UserDB, SQLiteConfig, sqlite3, User, UserOpt
users = UserDB(driver=sqlite3, config=SQLiteConfig)
 
#from userdb_mongo import UserDB, MongoConfig, User, UserOpt
#users = UserDB(config=MongoConfig)

# Better suggestion
# from userdb import UserDB
# from sqlite_config import SQLiteConfig
# from mongo_config import MongoConfig

# user = UserDB(config=SQLiteConfig)
# users = UserDB(config=MongoConfig)

users.connect()

# ASGI / WSGI compliant object
app = FastAPI()


@app.get("/users")
async def get_users():
    return users.get()

@app.post("/users")
async def add_user(user: User):
    users.add(user)

@app.get("/users/{name}")
async def get_user(name: str):
    await users.get(name)
    return list(users.get(name))[0]

@app.delete("/users/{name}")
async def delete_user(name):
    users.delete(name)

@app.patch("/users/{name}", status_code=status.HTTP_202_ACCEPTED)
async def update_user(name: str, user: UserOpt, response: Response):
    if not users.update(name, user):
        response.status_code = status.HTTP_404_NOT_FOUND

@app.put("/users/{name}", status_code=status.HTTP_202_ACCEPTED)
async def replace_user(name: str, user: User):
    users.replace(name, user)