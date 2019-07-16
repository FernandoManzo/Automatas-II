import pymysql

############### CONFIGURAR ESTO ###################
# Open database connection
db = pymysql.connect("localhost","root","","automatas")
##################################################

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to READ a record into the database.
sql = "SELECT * FROM alumnos".format(0)

# Execute the SQL command
cursor.execute(sql)

# Fetch all the rows in a list of lists.
results = cursor.fetchall()
for row in results:
   id = row[0]
   name = row[1]
   # Now print fetched result
   print ("id = {0}, name = {1}".format(id,name))

# disconnect from server
db.close()