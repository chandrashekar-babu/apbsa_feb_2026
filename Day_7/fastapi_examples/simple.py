from fastapi import FastAPI
from starlette.status import *
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    role: str

class UserOpt(BaseModel):
    name: Optional[str]
    role: Optional[str]

users = [
    User(name="john", role="admin"), 
    User(name="smith", role="developer")
]

# ASGI / WSGI compliant object
app = FastAPI()

@app.get("/")
async def show_root():
    return {"name": "john", "role": "admin"}

@app.get("/users")   # Collection resource
async def get_users():
    return users

@app.post("/users")
async def add_user(user: User):
    for u in users:
        print(u, user)
        if u.name == user.name:
            return JSONResponse(status_code=HTTP_409_CONFLICT,
                            content={"details": "Duplicate user name"})

    users.append(user)
    return JSONResponse(status_code=HTTP_201_CREATED,
                    content={"detail": "User record added"})

@app.get("/users/{name}") # Singular resource
async def get_user(name):
    # await users.get(name)
    for u in users:
        print(u)
        if u.name == name:
            return u
    else:
        return JSONResponse(
                status_code=HTTP_404_NOT_FOUND,
                content={"detail": "User record not found"})

@app.delete("/users/{name}") # Singular resource
async def delete_user(name):
    for u in users:
        if u.name == name:
            users.remove(u)
            return JSONResponse(
                status_code=HTTP_204_NO_CONTENT,
                content={"details": "User record removed"}
            )
    else:
        return JSONResponse(
                status_code=HTTP_404_NOT_FOUND,
                content={"detail": "User record not found"})

@app.put("/users/{name}") # Singular resource
async def replace_user(name, user: User):
    for i, u in enumerate(users):
        if u.name == name:
            users[i] = user    
            return JSONResponse(
                status_code=HTTP_202_ACCEPTED,
                content={"details": "User record removed"}
            )
    else:
        return JSONResponse(
                status_code=HTTP_404_NOT_FOUND,
                content={"detail": "User record not found"})

@app.patch("/users/{name}") # Singular resource
async def update_user(name, user: UserOpt):
    for u in users:
        print(u, user)
        if u.name == name:
            u.role = user.role    
            return JSONResponse(
                status_code=HTTP_202_ACCEPTED,
                content={"details": "User record removed"}
            )
    else:
        return JSONResponse(
                status_code=HTTP_404_NOT_FOUND,
                content={"detail": "User record not found"})

@app.get("/test/{x}/{y}/{z}")
async def testfn(x, y, z):
    return x + y + z