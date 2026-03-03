import falcon
import shelve
import json
from urllib.parse import parse_qs

TestsFormat = {
    "square": {
        "code": "base64 encoded marshalled function body",        
        "progress": "pending",
        "testcases": [
            dict(args=(2,), returns=4),
            dict(args=(3.0,), returns=9.0),
            dict(kwargs={"x": 4}, returns=16),
            dict(args=("Hello",), raises=("TypeError", "parameter must be number"))
        ]
    },

    "add": {
        "code": "base64'd function body...",
        "progress": "running test 3",
        "testcases": [
            dict(args=(1, 2), returns=3),
            dict(args=(10, 20, 30), returns=60),
            dict(args=("John", "Doe"), raises=("TypeError", "parameters must be numbers"))
        ]
    }

}

Tests = {}

# Collection resources generally support only GET and POST methods
class TestResource:
    def __init__(self):

    def on_get(self, req, resp):
        on_going = [ test for test in Tests if Tests[test]["progress"].startswith("running") ] 
        pending  = [ test for test in Tests if Tests[test]["progress"] == "pending" ]
        complete = [ test for test in Tests if Tests[test]["progress"] == "complete" ]            
        resp.body = json.dumps(dict(on_going=on_going, pending=pending, complete=complete))

    def on_post(self, req, resp):
        next_id = str(max((int(key) for key in TODOS.keys())) + 1)
        try:
            data = req.stream.read()
            print(data)
            TODOS[next_id] = json.loads(data)
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
            resp.body = json.dumps(dict(TODOS[todo_id]))

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
             TODOS[todo_id] = json.loads(data)
             resp.status = falcon.HTTP_202

    def on_patch(self, req, resp, todo_id):
        if todo_id not in TODOS:
            resp.status = falcon.HTTP_404
        else:
             data = req.stream.read()
             rec = TODOS[todo_id]
             rec.update(json.loads(data))
             TODOS[todo_id] = rec
             resp.status = falcon.HTTP_202


api = falcon.API()
api.add_route('/tests', TestsResource())
api.add_route('/tests/{test_id}', Todo())


