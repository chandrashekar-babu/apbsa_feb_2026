import sqlite3

CREATE_TABLE_SQL = """
    CREATE TABLE employees(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name VARCHAR(32) UNIQUE NOT NULL,
         dept VARCHAR(32))
"""

INSERT_SQL = """
    INSERT INTO employees(name, dept) VALUES(?,?)
"""

USERS = "charles", "david", "lynn", "linda", "emily", "smith", "jane"
DEPTS = "IT", "Marketing", "Operations", "IT", "Support", "Operations", "IT"
    
with sqlite3.connect("companydb") as conn:
    cursor = conn.cursor()
    try:
        cursor.execute(CREATE_TABLE_SQL)

        cursor.executemany(INSERT_SQL, zip(USERS, DEPTS))

    except Exception as e:
        print("Caught an exception: ", e)
        conn.rollback()
    
    else:
        conn.commit()



