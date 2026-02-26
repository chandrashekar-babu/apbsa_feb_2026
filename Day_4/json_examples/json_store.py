import json

a = {
    "name": "John",
    "scores": (23, 44, 55),
    "pass": True,
    "visited": None
}


with open("a.json", "w") as out:
    json.dump(a, out)
