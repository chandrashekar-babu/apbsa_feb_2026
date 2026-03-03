import falcon
from pymongo import MongoClient
import bson.json_util as json
import pdb

# Collection resources generally support only GET and POST methods

Required_task_keys = set(["name"])


class TodosResource:

    def __init__(self, tasks):
        self.tasks = tasks

    def on_get(self, req, resp):
        start = int(req.params.get("start", 0))
        length = int(req.params.get("len", 5))

        stop = start + length

        resp.body = json.dumps(self.tasks.find()[start:stop])

    def on_post(self, req, resp):
        try:
            data = req.stream.read()
            task = json.loads(data)
            #data = json.load(req.stream)

            #pdb.set_trace()

            if not task.keys() >= Required_task_keys:
                resp.status = falcon.HTTP_400
                print(task.keys(), Required_task_keys)
                print("failed with 400")
            elif self.tasks.find_one({"name": task["name"]}):
                resp.status = falcon.HTTP_409
                print("failed with 409")
            else:
                print("Inserting", task)
                self.tasks.insert_one(task)
                resp.status = falcon.HTTP_201
        except Exception as e:
            print(e)
            resp.status = falcon.HTTP_500


# A singular resource (record) should support GET, PUT, PATCH, DELETE


class Todo:
    def __init__(self, tasks):
        self.tasks = tasks

    def on_get(self, req, resp, name):
        rec = self.tasks.find_one({"name": name})
        if not rec:
            resp.status = falcon.HTTP_404
        else:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(rec)

    def on_delete(self, req, resp, name):
        if not self.tasks.find_one_and_delete({"name": name}):
            resp.status = falcon.HTTP_404
        else:
            resp.status = falcon.HTTP_204

    def on_put(self, req, resp, name):
        data = req.stream.read()
        task = json.loads(data)
        if not self.tasks.find_one_and_replace({"name": name}, task):
            resp.status = falcon.HTTP_404
        else:
            resp.status = falcon.HTTP_202

    def on_patch(self, req, resp, name):
        data = req.stream.read()
        task = json.loads(data)
        if not self.tasks.find_one_and_update({"name": name}, task):
            resp.status = falcon.HTTP_404
        else:
            resp.status = falcon.HTTP_202


conn = MongoClient()
db = conn.tasks_db
tasks = db.tasks


api = falcon.API()
api.add_route('/todos', TodosResource(tasks))
api.add_route('/todos/{name}', Todo(tasks))
