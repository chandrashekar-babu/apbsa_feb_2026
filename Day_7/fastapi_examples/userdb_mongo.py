from pydantic import BaseModel
from typing import Optional
from bson.objectid import ObjectId


class User(BaseModel):
    _id: ObjectId
    name: str
    password: str
    fullname: Optional[str]

class UserOpt(BaseModel):
    _id: ObjectId
    name: Optional[str]
    password: Optional[str]
    fullname: Optional[str]

from pymongo import MongoClient

class MongoConfig:
    dbname = "userdb_test"
    collection_name = "users"
    hostname = "172.26.111.13"
    port = 27017

class UserDB:
    def __init__(self, config):
        self.config = config()

    def connect(self):
        self.conn = MongoClient(host=self.config.hostname, port=self.config.port)
        self.database = self.conn[self.config.dbname]
        self.collection = self.database[self.config.collection_name]

    def create_schema(self):
        pass
 
    def add(self, user: User):
        self.collection.insert_one(user.dict())

    def get(self, username: str = None):
        if username is None:
            for user in self.collection.find():
                if user:
                    print(user)
                    u = User(**user)
                    #u.id = user["_id"]
                    yield u
        else:
            yield User(**self.collection.find_one({"name": username}))

    def delete(self, username: str):
        self.collection.delete_one({"name": username})

    def replace(self, username: str, user: User):
        self.collection.replace_one({"name": username}, user.dict())

    def update(self, username: str, user: UserOpt):
        print("user ->", user.dict())
        current_user = self.collection.find_one({"name": username})
        if current_user:
            current_user.update({k: v for k, v in user.dict().items() if v is not None})
            self.collection.update_one({"name": username}, { "$set": current_user })
            return True
        else:
            return False
            