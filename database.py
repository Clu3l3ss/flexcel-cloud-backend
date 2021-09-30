import config
import mysql.connector
from mysql.connector import errorcode

db = mysql.connector.connect(
    host=config.host,
    user=config.user,
    password=config.passwd
)

cursor = db.cursor()
db_name = 'flexcelcloud'


def create_database(cursor, database):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    cursor.execute("USE {}".format(db_name))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(db_name))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor, db_name)
        print("Database {} created successfully.".format(db_name))
        db.database = db_name
    else:
        print(err)
        exit(1)

#cursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, file_location VARCHAR(255))")

sql = "INSERT INTO users (user_id, file_location) VALUES (%s, %s)"
val = ("2", "/storage/Alice")
cursor.execute(sql, val)

db.commit()

#print(cursor.rowcount, "record inserted.")
