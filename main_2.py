#import, mydb e i cursori non serve ripeterli, basta dichiararli una volta sola

#creare tabella nel database
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase2"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


#mostrare le tabelle



mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

#creare una tabella con una primary key e il comando di auto incremento per riga

#mycursor.execute("CREATE TABLE customers2 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


#aggiungere una primary key ad una tabella gia esistente

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")