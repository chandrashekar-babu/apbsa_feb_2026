import falcon
from pymongo import MongoClient
import bson.json_util as json

conn = MongoClient()

db = conn.tododb
TODOS = db.todos

# Collection resources generally support only GET and POST methods


class TodosResource:
    def __init__(self):
        TODOS.insert_one({"todo_id": 0, "task": {}})

    def on_get(self, req, resp):
        resp.body = json.dumps(TODOS.find())

    def on_post(self, req, resp):
        next_id = max([r["todo_id"] for r in TODOS.find()]) + 1
        try:
            data = req.stream.read()
            print(data)
            TODOS.insert_one({"todo_id": next_id, "task": json.loads(data)})
        except Exception as e:
            print(e)
            resp.status = falcon.HTTP_405
        else:
            resp.status = falcon.HTTP_201

# A singular resource (record) should support GET, PUT, PATCH, DELETE


class Todo:

    def on_get(self, req, resp, todo_id):
        rec = TODOS.find_one({"todo_id": int(todo_id)})
        if not rec:
            resp.status = falcon.HTTP_404
        else:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(rec)

    def on_delete(self, req, resp, todo_id):
        if not TODOS.find_one_and_delete({"todo_id": int(todo_id)}):
            resp.status = falcon.HTTP_404
        else:
            resp.status = falcon.HTTP_204

    def on_put(self, req, resp, todo_id):
        data = req.stream.read()
        if not TODOS.find_one_and_replace({"todo_id": int(todo_id)},
                                          {"todo_id": int(todo_id),
                                           "task": json.loads(data)}):
            resp.status = falcon.HTTP_404
        else:
            resp.status = falcon.HTTP_202

    def on_patch(self, req, resp, todo_id):
        data = req.stream.read()
        if not TODOS.find_one_and_update({"todo_id": int(todo_id)},
                                         {"task": json.loads(data)}):
            resp.status = falcon.HTTP_404
        else:
            resp.status = falcon.HTTP_202


api = falcon.API()
api.add_route('/todos', TodosResource())
api.add_route('/todos/{todo_id}', Todo())

if __name__ == '__main__':
    api.run()
