import mariadb as driver

CREATE_TABLE_SQL="""CREATE TABLE users(
                               id INTEGER PRIMARY KEY AUTO_INCREMENT,
                               name VARCHAR(32) UNIQUE,
                               role VARCHAR(32)
                   )"""

INSERT_SQL="""INSERT INTO users(name, role) VALUES(?, ?)"""

DSN = dict(host="192.168.1.130",
            user="chandra",
            password="welcome", database="userdb1")

def connect():
    return driver.connect(**DSN)
