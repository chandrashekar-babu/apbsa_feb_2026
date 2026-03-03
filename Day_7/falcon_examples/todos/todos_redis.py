import falcon
import json
from urllib.parse import parse_qs
from redis import Redis

TODOS = Redis(db=1)

# Collection resources generally support only GET and POST methods


class TodosResource:
    def __init__(self):
        TODOS["0"] = {"task": None}

    def on_get(self, req, resp):
        resp.body = json.dumps({k: TODOS[k] for k in TODOS.keys()})

    def on_post(self, req, resp):
        next_id = str(max((int(key) for key in TODOS.keys())) + 1)
        try:
            data = req.stream.read()
            print(data)
            #TODOS[next_id] = json.loads(data)
            TODOS[next_id] = data
        except Exception as e:
            print(e)
            resp.status = falcon.HTTP_405
        else:
            resp.status = falcon.HTTP_201

# A singular resource (record) should support GET, PUT, PATCH, DELETE


class Todo:

    def on_get(self, req, resp, todo_id):
        if todo_id not in TODOS:
            resp.status = falcon.HTTP_404
        else:
            #resp.body = json.dumps(dict(TODOS[todo_id]))
            resp.body = TODOS[todo_id]

    def on_delete(self, req, resp, todo_id):
        if todo_id not in TODOS:
            resp.status = falcon.HTTP_404
        else:
            del TODOS[todo_id]
            resp.status = falcon.HTTP_204

    def on_put(self, req, resp, todo_id):
        if todo_id not in TODOS:
            resp.status = falcon.HTTP_404
        else:
            data = req.stream.read()
            #TODOS[todo_id] = json.loads(data)
            TODOS[todo_id] = data
            resp.status = falcon.HTTP_202

    def on_patch(self, req, resp, todo_id):
        if todo_id not in TODOS:
            resp.status = falcon.HTTP_404
        else:
            data = req.stream.read()
            rec = json.loads(TODOS[todo_id])
            rec.update(json.loads(data))
            TODOS[todo_id] = json.dumps(rec)
            resp.status = falcon.HTTP_202


api = falcon.API()
api.add_route('/todos', TodosResource())
api.add_route('/todos/{todo_id}', Todo())

if __name__ == '__main__':
    api.run()
