import sqlite3

SELECT_SQL = """
    SELECT * FROM employees
"""
    
with sqlite3.connect("companydb") as conn:
    cursor = conn.cursor()
    try:
        cursor.execute(SELECT_SQL)

        for row in cursor:
            print(row)

    except Exception as e:
        print("Caught an exception: ", e)
        conn.rollback()
    
    else:
        conn.commit()



