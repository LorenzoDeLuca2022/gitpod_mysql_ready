#Crea un programma che crei un DB chiamato Animali, contenente una tabella Mammiferi con i seguenti campi
#Id
#Nome_Proprio (varchar)
#Razza (varchar)
#Peso (int)
#Eta (int)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

#mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE Animali")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Mammiferi (id INT AUTO_INCREMENT PRIMARY KEY, Nome_proprio VARCHAR(255), Razza VARCHAR(255), Peso INT, Eta INT)")