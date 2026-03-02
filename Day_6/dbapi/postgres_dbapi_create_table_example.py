import psycopg2

CREATE_TABLE_SQL = """
    CREATE TABLE employees(
         id SERIAL,
         name VARCHAR(32) NOT NULL,
         dept VARCHAR(32))
"""

INSERT_SQL = """
    INSERT INTO employees(name, dept) VALUES(%s, %s)
"""

USERS = "charles", "david", "lynn", "linda", "emily", "smith", "jane"
DEPTS = "IT", "Marketing", "Operations", "IT", "Support", "Operations", "IT"
    
with psycopg2.connect(host="192.168.1.130", user="postgres", password="welcome", database="companydb") as conn:
    cursor = conn.cursor()
    try:
        cursor.execute(CREATE_TABLE_SQL)

        cursor.executemany(INSERT_SQL, list(zip(USERS, DEPTS)))

    except Exception as e:
        print("Caught an exception: ", e)
        conn.rollback()
    
    else:
        conn.commit()



