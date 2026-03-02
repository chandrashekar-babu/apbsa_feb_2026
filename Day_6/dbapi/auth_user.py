
def authorize(name, password):
    import sqlite3
    from hashlib import md5
    conn = sqlite3.connect("accessdb")

    select_sql = """
        SELECT COUNT(*) FROM users WHERE name = ? AND password = ? 
    """

    #select_sql = """
    #    SELECT COUNT(*) FROM users 
    #        WHERE name = '%s' AND 
    #        password = '%s'
    #"""

    cursor = conn.cursor()
    cursor.execute(select_sql, (name, md5(password).hexdigest()))
    #query = select_sql %  (name, md5(password).hexdigest())
    #print "Query = ", query
    #cursor.execute(query)
    numrows, = cursor.fetchone()
    conn.close()

    return bool(numrows)

if __name__ == '__main__':
    name = raw_input("Enter username: ")
    password = raw_input("Enter password: ")

    if authorize(name, password):
        print "User", name, "authorized"
    else:
        print "Invalid user"


