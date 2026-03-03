from fastapi import FastAPI

api = FastAPI()

@api.get("/hello")
async def hello_world():
    return {"name": "John"}

