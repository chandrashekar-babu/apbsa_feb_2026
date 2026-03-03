from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status
from starlette.responses import JSONResponse
from typing import Optional

class User(BaseModel):
    name: str
    role: str
    score: float

class UserUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    score: Optional[float] = None


app = FastAPI()

users = { }

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}


@app.get("/users")
def get_users():
    return users

@app.post("/users")
def create_user(user: User):
    users[user.name] = user
    return JSONResponse(content={"status": "created"}, 
                        status_code=status.HTTP_201_CREATED)

@app.get("/users/{user_name}")
def get_user(user_name: str):
    user = users.get(user_name)
    if user:
        return user
    else:
        return JSONResponse(content={"status": "not found"}, 
                            status_code=status.HTTP_404_NOT_FOUND)
    
@app.delete("/users/{user_name}")
def delete_user(user_name: str):
    if user_name in users:
        del users[user_name]
        return JSONResponse(content=None, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"status": "not found"}, 
                            status_code=status.HTTP_404_NOT_FOUND)

@app.patch("/users/{user_name}")
def update_user(user_name: str, user: UserUpdate):
    if user_name in users:
        if user.role is not None:
            users[user_name].role = user.role
        if user.score is not None:
            users[user_name].score = user.score
               
        return JSONResponse(content={"status": "updated"}, 
                            status_code=status.HTTP_202_ACCEPTED)
    else:
        return JSONResponse(content={"status": "not found"}, 
                            status_code=status.HTTP_404_NOT_FOUND)

@app.put("/users/{user_name}")
def replace_user(user_name: str, user: User):
    if user_name in users:
        users[user_name] = user
        return JSONResponse(content={"status": "replaced"}, 
                            status_code=status.HTTP_202_ACCEPTED)
    else:
        return JSONResponse(content={"status": "not found"}, 
                            status_code=status.HTTP_404_NOT_FOUND)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    