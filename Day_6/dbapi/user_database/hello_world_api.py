from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    dept: str


app = FastAPI()

@app.get("/")
async def home():
    return {"message": "hello world"}

@app.get("/users")
async def get_users():
    return [{"name": "john"}, {"name": "smith"}, {"name": "sarah"}]

@app.post("/users")
async def post_users(user: User):
    print(f"Got user: {user.name=}, {user.dept=}")
    
