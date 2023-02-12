#import, mydb e i cursori non serve ripeterli, basta dichiararli una volta sola

#seleziona tutte le righe della tabella, le estrae e le printa
#se voglio selezionare solo la prima riga uso fetchone() e non fetchall()
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase2"
)

mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM customers")

#myresult = mycursor.fetchall()

#for x in myresult:
 # print(x)

#stessa cosa di prima, ma non seleziona tutte le colonne ma solo quelle scelte

#mycursor.execute("SELECT name, address FROM customers")

#myresult = mycursor.fetchall()

#for x in myresult:
 # print(x)


