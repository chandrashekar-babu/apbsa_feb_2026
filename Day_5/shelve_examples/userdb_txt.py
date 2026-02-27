def parse_users(filename):
    users = {}
    with open(filename) as source:
        for line in source:
            line = line.strip()
            if not line: continue
            name, password, fullname = line.split(":")
            rec = {"name": name, 
                   "password": password, 
                   "fullname": fullname}
            users[name] = rec
    return users


def store_users(users, filename):
    with open(filename, "w") as out:
        for rec in users.values():
            out.write("{}:{}:{}\n".format(
                                rec["name"],
                                rec["password"],
                                rec["fullname"]))

def convert_to_shelve(users, filename):
    import shelve
    out = shelve.open(filename)
    out.update(users)
    out.close()
    
if __name__ == '__main__':
    
    users = parse_users("users.txt")
    users["smith"]["password"] = "welcome123"
    store_users(users, "users_new.txt")    
