from pymongo import MongoClient
from time import ctime
from pprint import pprint

client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017/')
db = client.test_database
collection = db.test_collection

post = {
    "author": "John Doe",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
             "date": ctime()
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

print(db.collection_names(include_system_collections=False))
pprint(posts.find_one())

