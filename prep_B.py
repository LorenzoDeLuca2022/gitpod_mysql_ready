import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (Nome_proprio) VALUES (%s)"
val = [
    ("Cane",),
    ("Gatto",),
    ("Cacatua",),
    ("Corvo",),
    ("Lupo",)
]

mycursor.executemany(sql, val)

mydb.commit()