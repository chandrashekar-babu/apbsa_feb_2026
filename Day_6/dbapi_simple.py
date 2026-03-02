#import db_sqlite3_config as config
#import db_mariadb_config as config
import db_postgres_config as config

from itertools import count

with config.driver.connect(**config.connection_params) as conn:
    cursor = conn.cursor()
    cursor.execute(config.CREATE_STAFF)
    
    for i in count(1):
        print(f"Row {i}:")
        name = input("   Enter name: ")
        role = input("   Enter role: ")
        dept = input("   Enter dept: ")
        cursor.execute(config.INSERT_STAFF, (name, role, dept))
        choice = input("Add new row (y/n) ? ")
        if choice[0] not in 'Yy':
            break
    
    print("-" * 40)
    cursor.execute(config.SELECT_ALL_STAFF)
    for i, name, role, dept in cursor:
        print(f"{i}. {name=}, {role=}, {dept=}")
        
