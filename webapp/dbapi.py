#   zdefiniowanie właściwości połączenia
dbconfig = { 'host': '127.0.0.1',
              'user': 'vsearch',
              'password': 'Na fali1',
              'database': 'vsearchlogDB', }

#   importowanie sterownika bazy danych
import mysql.connector

#   nawiązanie połączenia i utworzenie kursora
conn = mysql.connector.connect(**dbconfig)

cursor = conn.cursor()

#   przypisanie do zmiennej łańcucha znakowego zawierającego zapytanie
_SQL = """insert into log
          (phrase, letters, ip, browser_string, results)
          values
          (%s, %s, %s, %s, %s)"""

#   wysyłanie zapytania do serwera
cursor.execute(_SQL, ('galaktyka', 'tym', '127.0.0.1', 'Opera', "{'t', 'y'}"))

#   wymuszenie zapisu danych w bazie danych
conn.commit()

#   pobranie z tabeli i wyświetlenie wiersz po wierszu danych
_SQL = """select * from log"""

cursor.execute(_SQL)

for row in cursor.fetchall():
    print(row)

#   sprzątanie po połączeniu
cursor.close()

conn.close()
