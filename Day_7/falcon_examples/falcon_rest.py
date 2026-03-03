import falcon
import json

post_data = [{"author": "Smith", "title": "test resource"}]

class PostResource:

    def on_get(self, req, resp):
        resp.data = bytes(json.dumps(post_data[0]), "utf8")

    def on_post(self, req, resp):
        post_data.append(json.loads(req.data))
        print(post_data)



api = falcon.API()
api.add_route("/post", PostResource())
