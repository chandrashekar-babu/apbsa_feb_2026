from fastapi import FastAPI
from pydantic import BaseModel
from starlette.status import HTTP_201_CREATED

class User(BaseModel):
    name: str
    fullname: str

# ASGI / WSGI compliant object
app = FastAPI()

@app.get("/")
async def read_root():
    """Get the root resource..."""
    #await get_result_of_along_query()
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, city: str, q: int = 0):
    return {"item_id": item_id, "q": q, "city": city}

@app.post("/users", status_code=HTTP_201_CREATED)
async def create_users(user: User):
    print(f"Got POST request: name = {user.name}, fullname: {user.fullname}")
    return {"id": 100}

# Resource-Oriented-Architecture (ROA)
# Collection resource / Plural resource
   # - GET -- Retrieve a collection of resources / documents
   # - POST -- Insert a new document/resource into a collection

# Singular resource
   # - GET /users/1  -> Retrieve a single resource
   # - PUT /users/1  -> Replace a  single resource
   # - PATCH /users/1 -> Update a single resource
   # - DELETE /users/1 -> Delete a resourced identified by 1