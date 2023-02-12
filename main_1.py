#import, mydb e i cursori non serve ripeterli, basta dichiararli una volta sola

#creare un database in mysql

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

#mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase2")



#ciclo for per leggere ogni riga di output del database (elenco database disponibili)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


#permette di connettersi al database (se non mosta nulla è giusto, perchè non da errore)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase2"
)