#Scrivi un programma che Chieda all’utente se vuole inserire un nuovo animale per 5 volte.
#Nota: ogni volta deve inserire tutti i dati.
#Utilizza il programma al punto B per verificare che i nuovi animali siano stati inseriti correttamente
#Opzionale: Verifica se gli interi sono effettivamente interi, se non lo sono mostra un messaggio di errore

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

for x in range(2):
    Nome = input("Inserisci il nome del nuovo animale: ");
    Razza = input("Inserisci la razza del nuovo animale: ");
    Peso = int(input("Inserisci il peso del nuovo animale: "));
    Eta =int(input("Inserisci l'eta del nuovo animale: "));

    query = "INSERT INTO Mammiferi (Nome_proprio, Razza, Peso, Eta) VALUES (%s,%s,%d,%d)"
    values = ( Nome, Razza, Peso, Eta)
    mycursor.execute(query, values)
    mydb.commit()
    print("Valori inseriti correttamente nella tabella Mammiferi")

mycursor.close()
mydb.close()

