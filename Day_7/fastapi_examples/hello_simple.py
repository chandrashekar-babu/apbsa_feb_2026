from fastapi import FastAPI

# ASGI / WSGI compliant object
app = FastAPI()

@app.get("/")
async def show_root():
    return {"name": "john", "role": "admin"}
