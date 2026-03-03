from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status
from starlette.responses import JSONResponse

class User(BaseModel):
    name: str
    role: str
    score: float

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
    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    