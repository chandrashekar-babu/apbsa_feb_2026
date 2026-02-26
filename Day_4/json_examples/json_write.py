import json

# numbers - int, float
# strings - bytes, str
# tuple, list, set  --> json array
# dictionary --> json object
# True / False -> true / false
# None --> null

info = {
    "name"  : "john",
    "city"  : "delhi",
    "age"   : 30,
    "active" : True,
    "travelled" : None,
    "owns"  : { "car" : "ferrari", "bike" : "yamaha" },
    "visited" : ["mumbai", ("kolkatta", "bengaluru") ]
}


with open("data.json", "w") as out:
    json.dump(info, out)


