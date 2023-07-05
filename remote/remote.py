import csv

import simplejson as simplejson

import psycopg

from result import PomiarView

with open("db_credentials.json") as f:
    dane = simplejson.loads(f.read())

connection = psycopg.connect(
    host=dane["host"],
    user=dane["user"],
    dbname=dane["database"],
    password=dane["password"],
    port=dane["port"])

cur = connection.cursor()


def create_tables():
    cur.execute("CREATE TABLE IF NOT EXISTS osoba(id INT NOT NULL, imie VARCHAR(64) NOT NULL, nazwisko VARCHAR(64) NOT NULL, email VARCHAR(128), PRIMARY KEY(id));")
    cur.execute("CREATE TABLE IF NOT EXISTS licznik(id INT NOT NULL, id_osoby INT NOT NULL, adres VARCHAR(256), PRIMARY KEY(id));")
    cur.execute("CREATE TABLE IF NOT EXISTS pracownicy(id INT NOT NULL, imie VARCHAR(64) NOT NULL, nazwisko VARCHAR(64) NOT NULL, miejsce_zatrudnienia VARCHAR(128), PRIMARY KEY(id));")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS pomiary(id_licznika INT NOT NULL, id_pracownika INT NOT NULL, data DATE, taryfa VARCHAR(64), energia_czynna FLOAT,
        energia_oddana FLOAT, energia_q1 FLOAT, energia_q2 FLOAT, energia_q3 FLOAT, energia_q4 FLOAT, maks_moc FLOAT);
        """)

    connection.commit()


def drop_tables():
    cur.execute("DROP TABLE IF EXISTS osoba;")
    cur.execute("DROP TABLE IF EXISTS licznik;")
    cur.execute("DROP TABLE IF EXISTS pracownicy;")
    cur.execute("DROP TABLE IF EXISTS pomiary;")

    connection.commit()


def fetch_data(date_start, date_end):
    cur.execute("""
    SELECT osoba.imie || ' ' || osoba.nazwisko AS owner, pracownicy.imie || ' ' ||  pracownicy.nazwisko AS pracownnik,
    licznik.adres, pomiary.data, pomiary.taryfa, pomiary.energia_czynna, pomiary.energia_oddana, pomiary.energia_q1, 
    pomiary.energia_q2, pomiary.energia_q3, pomiary.energia_q4, pomiary.maks_moc FROM pomiary 
    JOIN licznik ON licznik.id = pomiary.id_licznika JOIN osoba ON osoba.id = licznik.id_osoby JOIN pracownicy 
    ON pracownicy.id = pomiary.id_pracownika WHERE pomiary.data BETWEEN %s AND %s ORDER BY pomiary.data ASC;
    """, (date_start, date_end,))

    views = []
    for row in cur.fetchall():
        views.append(PomiarView(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))
    return views


def import_data_to_postgres():
    import_osoby_from_csv_to_postgres()
    import_liczniki_from_csv_to_postgres()
    import_pracownicy_from_csv_to_postgres()
    import_pomiary_from_csv_to_postgres()


def import_osoby_from_csv_to_postgres():
    with open('../osoby.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';',  quotechar='|')
        for row in reader:
            print(row)
            cur.execute(
                "INSERT IGNORE INTO osoba VALUES (%s, %s, %s, %s);", tuple(row))

    connection.commit()


def import_liczniki_from_csv_to_postgres():
    with open('../liczniki.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';',  quotechar='|')
        for row in reader:
            cur.execute(
                "INSERT IGNORE INTO licznik VALUES (%s, %s, %s);", row)

    connection.commit()


def import_pracownicy_from_csv_to_postgres():
    with open('../pracownicy.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';',  quotechar='|')
        for row in reader:
            cur.execute(
                "INSERT IGNORE INTO pracownicy VALUES (%s, %s, %s, %s);", row)

    connection.commit()


def import_pomiary_from_csv_to_postgres():
    with open('../pomiary.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';',  quotechar='|')
        for row in reader:
            cur.execute(
              "INSERT IGNORE INTO pomiary VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", row)

    connection.commit()
