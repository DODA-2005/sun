import mysql.connector as mylo

# Correcting connection parameters and method names
db = mylo.connect(host="localhost", user="root", passwd="", database="your_database_name")
cursor = db.cursor()

# Fixing the SQL query syntax and cursor method
sql = "UPDATE student SET grade = 'A' WHERE ports > 6"

try:
    cursor.execute(sql)
    db.commit()
except mylo.Error as e:
    print("An error occurred:", e)
    db.rollback()
finally:
    cursor.close()
    db.close()
