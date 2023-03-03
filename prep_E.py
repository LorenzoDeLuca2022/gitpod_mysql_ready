#Scrivi un programma che visualizza tutti gli animali che pesano più di 2 kg

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Mammiferi where Peso > 2")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)