import json

#json.dump(user_info, open("json.dat", "wb"))
with open("a.json") as infile:
    d = json.load(infile)

for k, v in d.items(): print(k, "=", v)
print(d)
