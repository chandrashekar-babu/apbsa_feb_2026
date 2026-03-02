import mariadb

CREATE_TABLE_SQL = """
    CREATE TABLE IF NOT EXISTS employees(
         id INTEGER PRIMARY KEY AUTO_INCREMENT,
         name VARCHAR(32) UNIQUE NOT NULL,
         dept VARCHAR(32))
"""

INSERT_SQL = """
    INSERT INTO employees(name, dept) VALUES(?,?)
"""

USERS = "charles", "david", "lynn", "linda", "emily", "smith", "jane"
DEPTS = "IT", "Marketing", "Operations", "IT", "Support", "Operations", "IT"
    
with mariadb.connect(host="192.168.1.130", user="chandra", password="welcome", database="companydb") as conn:
    cursor = conn.cursor()
    try:
        cursor.execute(CREATE_TABLE_SQL)

        cursor.executemany(INSERT_SQL, list(zip(USERS, DEPTS)))

    except Exception as e:
        print("Caught an exception: ", e)
        conn.rollback()
    
    else:
        conn.commit()



