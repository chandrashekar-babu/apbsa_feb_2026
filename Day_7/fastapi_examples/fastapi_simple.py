from fastapi import FastAPI # ASGI compliant class -> successor of WSGI ()
from starlette.status import HTTP_201_CREATED
from starlette.responses import JSONResponse

from pydantic import BaseModel

class User(BaseModel):
    name: str
    role: str
    score: float

api = FastAPI()

@api.get("/")
async def hello_world():
    return {"hello": "world"}

@api.post("/users")
async def store_data(u: User):
    print("Storing ", u)
    return JSONResponse(content={"status" :"created"}, status_code=HTTP_201_CREATED)

@api.get("/users")
async def get_users():
    # TODO
    return [{"name": "John", "role": "Admin"}]
