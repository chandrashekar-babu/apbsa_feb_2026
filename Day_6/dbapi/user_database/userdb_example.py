import userdb_sqlite as userdb
#import userdb_mariadb as userdb
#import userdb_postgres as userdb


data = [
 ('guido', 'guido123', 'IT', 'Developer'),
 ('emily', 'em345', 'IT', 'Developer'),
 ('david', 'dave234', 'IT', 'Support')
]


if __name__ == '__main__':
    with userdb.driver.connect(**userdb.CONNECTION) as conn:
        cursor = conn.cursor()

        try:
            cursor.execute(userdb.CREATE_TABLE_SQL)

            cursor.executemany(userdb.INSERT_SQL, data)
        except Exception as e:
            print("Caught exception while inserting rows: ", e)
            conn.rollback()
        else:
            print("Inserted a few rows in users table")
            conn.commit()

        try:
            cursor.execute(userdb.SELECT_ALL_SQL)
        except Exception as e:
            print("Caught exception while selecting rows: ", e)
            #conn.rollback()
        else:
            print("Fetching  rows in users table")
            for row in cursor:
                print(row)

            #conn.commit()

 
