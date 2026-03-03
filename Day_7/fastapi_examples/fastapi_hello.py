from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse

from pydantic import BaseModel

class User(BaseModel):
    name: str
    dept: str
    age:  int
    
api = FastAPI()

@api.get("/hello")
def hello_world():
    return {"hello": "world"}

@api.get("/about", response_class=HTMLResponse)
def about_me():
    return "<h1>This is a simple html fragment</h1>"

@api.get("/welcome", response_class=PlainTextResponse)
def welcome_page():
    return "Welcome to FastAPI application"

@api.post("/users")
def add_user(user: User):
    print("add_user invoked: user =", user)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=user.__dict__)