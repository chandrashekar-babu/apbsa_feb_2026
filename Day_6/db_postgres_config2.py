import psycopg2 as driver

config = {
    "connection_params": {
        "host": "localhost",
        "user": "testuser",
        "password": "w3lc0me",
        "database": "newdb"
    },
    "create_staff": """
            CREATE TABLE IF NOT EXISTS staff
            (
                id   SERIAL,
                name VARCHAR(32),
                role VARCHAR(32),
                dept VARCHAR(32)
            )
    """,

    "insert_staff":  """
            INSERT INTO staff (name, role, dept) 
            VALUES(%s, %s, %s)
    """,

    "select_all_staff":  "SELECT * FROM staff"
}