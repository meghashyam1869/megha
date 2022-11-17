import pymysql

#connect to the database

db=pymysql.connect(host='localhost',
                   user='root',
                   password='admin',
                   database='demo',
                   cursorclass=pymysql.cursors.DictCursor)

cursor=db.cursor()

cursor.execute("SELECT VERSION()")

data=cursor.fetchone()

print("Database version:%s"%data)
