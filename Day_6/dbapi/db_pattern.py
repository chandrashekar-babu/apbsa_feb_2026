import sqlite3

try:
    conn = sqlite3.connect("empdb")
    cursor = conn.cursor

    cursor.execute(update_sql1)
    cursor.execute(update_sql2)

except OperationalError as e:
    print "Exception thrown..."
    conn.rollback()

except Exception as e:
    conn.rollback()
    
else:
    conn.commit()
finally:
    conn.close()

