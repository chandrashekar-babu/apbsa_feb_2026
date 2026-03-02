import mariadb_config as db

if __name__ == '__main__':
    rows = [("adrian", "support"), ("charles", "development"), ("david", "marketing"),
            ("emily", "development")]

    with db.connect() as conn:
        cursor = conn.cursor()
        cursor.execute(db.CREATE_TABLE_SQL)
        cursor.executemany(db.INSERT_SQL, rows)
        conn.commit()
