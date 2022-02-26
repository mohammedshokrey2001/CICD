import MySQLdb
db = MySQLdb.connect("mysql-server","root","secret","mydb")
cursor = db.cursor()
cursor.execute("SELECT * FROM person")
data = cursor.fetchone()
fname = data[0]
lname = data[1]
print ("fname=%s, lname=%s" % (fname, lname))
db.close()


          
          