import pymysql

#connect to the database

db=pymysql.connect(host='localhost',
                        user='root',
                        password='admin',
                        database='demo',
                        cursorclass=pymysql.cursors.DictCursor)

cursor=db.cursor()
###query='INSERT INTO employee VALUES("megha","shyam",48)'
##query="delete from employee where id=48"
query="alter employee add mail varchar(20)"
try:

    cursor.execute(query)
    db.commit()
except:
    db.rollback()
db.close
