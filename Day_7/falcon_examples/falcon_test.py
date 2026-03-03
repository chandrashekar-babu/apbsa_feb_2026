import falcon
import json
import urllib.parse

blog_data = {"blog_id": "testblog": "skdljf kljflkjsdklfjsdlkfjsdklfj sdlfk"}


class BlogResource:
    def on_get(self, req, resp, blog_id=None):
        resp.body = json.dumps(dict(**blog_data, blog_id=blog_id))

    def on_post(self, req, resp):
        data = req.stream.read()
        blog_data.update(json.loads(data))

        resp.status = falcon.HTTP_201


class HelloResource:
    def on_get(self, req, resp):
        resp.body = json.dumps({"message": "Hello world"})
        print(req.query_string)
        print(req.params)


api = falcon.API()
api.add_route('/blog/{blog_id}', BlogResource())
api.add_route('/blog', BlogResource())
api.add_route("/hello", HelloResource())

if __name__ == '__main__':
    api.run()
