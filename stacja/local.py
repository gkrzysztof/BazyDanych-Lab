import sqlite3

from stacja.csv_exporter import export_osoby_to_csv, export_liczniki_to_csv, export_pracownicy_csv, export_pomiary_to_csv
from common.model import Licznik, Osoba, Pracownik, Pomiary


conn = sqlite3.connect("../liczniki.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS osoba(id INT NOT NULL, imie VARCHAR(64) NOT NULL, nazwisko VARCHAR(64) NOT NULL, email VARCHAR(128), PRIMARY KEY(id));")
cur.execute("CREATE TABLE IF NOT EXISTS licznik(id INT NOT NULL, id_osoby INT NOT NULL, adres VARCHAR(256), PRIMARY KEY(id));")
cur.execute("CREATE TABLE IF NOT EXISTS pracownicy(id INT NOT NULL, imie VARCHAR(64) NOT NULL, nazwisko VARCHAR(64) NOT NULL, miejsce_zatrudnienia VARCHAR(128), PRIMARY KEY(id));")
cur.execute("""
CREATE TABLE IF NOT EXISTS pomiary(id_licznika INT NOT NULL, id_pracownika INT NOT NULL, data DATE, taryfa VARCHAR(64), energia_czynna FLOAT,
energia_oddana FLOAT, energia_q1 FLOAT, energia_q2 FLOAT, energia_q3 FLOAT, energia_q4 FLOAT, maks_moc FLOAT);
""")
conn.commit()


def create_osoba(id, imie, nazwisko, email):
    osoba = Osoba(id, imie, nazwisko, email)

    cur.execute("INSERT INTO osoba(id, imie, nazwisko, email) VALUES(?, ?, ?, ?)", (osoba.id, osoba.imie, osoba.nazwisko, osoba.email))
    conn.commit()
    return osoba


def create_licznik(id, id_osoby, adres):
    licznik = Licznik(id, id_osoby, adres)

    cur.execute("INSERT INTO licznik(id, id_osoby, adres) VALUES(?, ?, ?)", (licznik.id, licznik.id_osoby, licznik.adres))
    conn.commit()
    return licznik


def create_pracownik(id, imie, nazwisko, miejsce_zatrudnienia):
    pracownik = Pracownik(id, imie, nazwisko, miejsce_zatrudnienia)

    cur.execute("INSERT INTO pracownicy(id, imie, nazwisko, miejsce_zatrudnienia) VALUES(?, ?, ?, ?)", (pracownik.id, pracownik.imie, pracownik.nazwisko, pracownik.miejsce_zatrudnienia))
    conn.commit()
    return pracownik


def create_pomiar(id_licznika, id_pracownika, data, taryfa, energia_czynna, energia_oddana, energia_q1, energia_q2, energia_q3, energia_q4, maks_moc):
    pomiar = Pomiary(id_licznika, id_pracownika, data, taryfa, energia_czynna, energia_oddana, energia_q1, energia_q2, energia_q3, energia_q4, maks_moc)

    cur.execute("""
    INSERT INTO pomiary(id_licznika, id_pracownika, data, taryfa, energia_czynna, energia_oddana, energia_q1, energia_q2, energia_q3, energia_q4, maks_moc)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (pomiar.id_licznika, pomiar.id_pracownika, pomiar.data, pomiar.taryfa, pomiar.energia_czynna, pomiar.energia_oddana, pomiar.energia_q1, pomiar.energia_q2, pomiar.energia_q3, pomiar.energia_q4, pomiar.maks_moc))
    conn.commit()
    return pomiar


def store_all(osoby, liczniki, pracownicy, pomiary):
    for osoba in osoby:
        cur.execute("INSERT INTO osoba(id, imie, nazwisko, email) VALUES(?, ?, ?, ?)",
                    (osoba.id, osoba.imie, osoba.nazwisko, osoba.email))
    conn.commit()

    for licznik in liczniki:
        cur.execute("INSERT INTO licznik(id, id_osoby, adres) VALUES(?, ?, ?)",
                    (licznik.id, licznik.id_osoby, licznik.adres))
    conn.commit()

    for pracownik in pracownicy:
        cur.execute("INSERT INTO pracownicy(id, imie, nazwisko, miejsce_zatrudnienia) VALUES(?, ?, ?, ?)",
                    (pracownik.id, pracownik.imie, pracownik.nazwisko, pracownik.miejsce_zatrudnienia))
    conn.commit()

    for pomiar in pomiary:
        cur.execute("""
        INSERT INTO pomiary(id_licznika, id_pracownika, data, taryfa, energia_czynna, energia_oddana, energia_q1, energia_q2, energia_q3, energia_q4, maks_moc)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (pomiar.id_licznika, pomiar.id_pracownika, pomiar.data, pomiar.taryfa, pomiar.energia_czynna, pomiar.energia_oddana, pomiar.energia_q1, pomiar.energia_q2, pomiar.energia_q3, pomiar.energia_q4, pomiar.maks_moc))
    conn.commit()


def load_all():
    cur.execute("SELECT * FROM osoba")
    osoby = []
    for row in cur.fetchall():
        osoby.append(Osoba(row[0], row[1], row[2], row[3]))
    cur.execute("SELECT * FROM licznik")
    liczniki = []
    for row in cur.fetchall():
        liczniki.append(Licznik(row[0], row[1], row[2]))
    cur.execute("SELECT * FROM pracownicy")
    pracownicy = []
    for row in cur.fetchall():
        pracownicy.append(Pracownik(row[0], row[1], row[2], row[3]))
    cur.execute("SELECT * FROM pomiary")
    pomiary = []
    for row in cur.fetchall():
        pomiary.append(Pomiary(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
    return osoby, liczniki, pracownicy, pomiary


def export_all_to_csv():
    osoby, liczniki, pracownicy, pomiary = load_all()

    export_osoby_to_csv(osoby)
    export_liczniki_to_csv(liczniki)
    export_pracownicy_csv(pracownicy)
    export_pomiary_to_csv(pomiary)
