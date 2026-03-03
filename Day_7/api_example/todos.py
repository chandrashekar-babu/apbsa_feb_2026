from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response
from starlette.status import HTTP_201_CREATED

class TodoItem(BaseModel):
    title: str
    description: str
    date: str
    value: float

#def get_db():
#    from pymongo import MongoClient
#    conn = MongoClient()
#    tododb = conn.todos
#    return tododb.todos


class Todos:
    def __init__(self):
        self.todos = {}
        self.last_inserted_id = 0

    def find(self):
        return list(self.todos.values())

    def insert_one(self, todo):
        todo_id = self.last_inserted_id
        self.todos[todo_id] = todo
        self.last_inserted_id += 1
        return todo_id

    def find_one(self, todo_id):
        return self.todos.get(todo_id)

def get_db():
    return Todos()

app = FastAPI()

todos = get_db()

@app.get("/todos")
def get_todos():
    """Return a list of todos
       Each todo will have a title and description
    """
    return todos.find()

@app.post("/todos", status_code=HTTP_201_CREATED)
def post_todo(todo: TodoItem, response: Response):
    return todos.insert_one(todo.dict())

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    return todos.find_one(todo_id)
