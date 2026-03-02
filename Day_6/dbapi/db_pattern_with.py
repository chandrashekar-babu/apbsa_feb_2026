import sqlite3

with sqlite.connect("empdb") as conn:
    cursor = conn.cursor()

    try:
        cursor.execute(update_sql1)
        cursor.execute(update_sql2)
    except OperationalError as e:
        print("Exception thrown...")
        conn.rollback()
    else:
        conn.commit()
