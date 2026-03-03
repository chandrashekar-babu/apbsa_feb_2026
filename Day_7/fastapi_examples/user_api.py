import sqlite3 as driver
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.status import *

from pydantic import BaseModel

INSERT_SQL = """
INSERT INTO users(name, password, fullname) VALUES(?,?,?)
"""

class User(BaseModel):
    name: str
    fullname: str
    password: str

api = FastAPI()


@api.get("/users")
async def get_users():
    with driver.connect("userdb") as conn:
        cursor = conn.execute("SELECT name, fullname from users")
        result = [ User(name=name, fullname=fullname, password="[hidden]") \
            for name, fullname in cursor ]
    return result

@api.post("/users")
async def insert_user(user: User):
    with driver.connect("userdb") as conn:
        cursor = conn.cursor()
        cursor.execute(INSERT_SQL, (user.name, user.password, user.fullname))
        conn.commit()

    #return JSONResponse(status_code=HTTP_406_NOT_ACCEPTABLE,
    #                content={"reason": "User record required"})


@api.get("/users/{name}")
async def get_user(name: str):
    with driver.connect("userdb") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, fullname from users WHERE name = ?",
                              (name,))
        name, fullname = cursor.fetchone()
    return User(name=name, fullname=fullname, password="[hidden]")

@api.patch("/users")
async def update_user(user: User):
    pass

@api.put("/users")
async def replace_user(user: User):
    pass

@api.delete("/users/{name}")
async def delete_user(name: str):
    pass
