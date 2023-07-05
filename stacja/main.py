import os
import re
import sqlite3

from local import store_all, create_osoba, create_pracownik, create_licznik, create_pomiar, export_all_to_csv
from common.model import *


here = os.path.abspath(os.path.dirname(__file__))
version = re.search(
    '^__version__\s*=\s*"(.*)"', open(os.path.join(here, "__init__.py")).read(), re.M
).group(1)
release = re.search(
    '^__release__\s*=\s*"(.*)"', open(os.path.join(here, "__init__.py")).read(), re.M
).group(1)
__version__ = version
__release__ = release


def generate_example_data():
    osoby = [
        Osoba(1, "Jan", "Kowalski", "jan.kowalski@gmail.com"),
        Osoba(2, "Adam", "Nowak", "adam.nowak@gmail.com"),
        Osoba(3, "Anna", "Kowalska", "anna.kowalski@gmail.com"),
        Osoba(4, "Jan", "Nowak", "jan.nowak@gmail.com")
    ]

    liczniki = [
        Licznik(1, 1, "ul. Kowalska 1, 00-001 Warszawa"),
        Licznik(2, 2, "ul. Nowak 1, 00-001 Warszawa"),
        Licznik(3, 3, "ul. Kowalska 2, 00-001 Warszawa"),
        Licznik(4, 4, "ul. Nowak 2, 00-001 Warszawa")
    ]

    pracownicy = [
        Pracownik(1, "Chris", "Gora", "Warszawa"),
        Pracownik(2, "Mgr. Inz. Woyciech", "Haynow'sky", "Warszawa"),
        Pracownik(3, "Eric", "Mikey", "Warszawa"),
    ]

    pomiary = [
        Pomiary(1, 1, "2023-06-22", "G12", 100.0, 40.0, 20.0, 19.4, 21.4, 19.3, 2000),
        Pomiary(2, 2, "2023-06-22", "G12", 100.0, 50.0, 17.1, 19.2, 18.9, 12.1, 3900),
        Pomiary(3, 3, "2023-06-22", "G12", 100.0, 60.0, 19.1, 19.2, 19.3, 19.4, 4000),
        Pomiary(4, 4, "2023-06-22", "G12", 100.0, 70.0, 19.1, 19.2, 19.3, 19.4, 5000),

        Pomiary(1, 1, "2023-06-23", "G12", 100.0, 36.0, 20.0, 19.4, 21.4, 19.3, 2000),
        Pomiary(2, 2, "2023-06-23", "G12", 100.0, 51.0, 17.1, 19.2, 18.9, 12.1, 3900),
        Pomiary(3, 3, "2023-06-23", "G12", 100.0, 64.0, 19.1, 19.2, 19.3, 19.4, 4000),
        Pomiary(4, 4, "2023-06-23", "G12", 100.0, 69.0, 19.1, 19.2, 19.3, 19.4, 5000),

        Pomiary(1, 1, "2023-06-24", "G12", 100.0, 49.0, 20.0, 19.4, 21.4, 19.3, 2000),
        Pomiary(2, 2, "2023-06-24", "G12", 100.0, 70.0, 17.1, 19.2, 18.9, 12.1, 3900),
        Pomiary(3, 3, "2023-06-24", "G12", 100.0, 63.0, 19.1, 19.2, 19.3, 19.4, 4000),
        Pomiary(4, 4, "2023-06-24", "G12", 100.0, 71.0, 19.1, 19.2, 19.3, 19.4, 5000),

        Pomiary(1, 1, "2023-06-25", "G12", 100.0, 41.0, 20.0, 19.4, 21.4, 19.3, 2000),
        Pomiary(2, 2, "2023-06-25", "G12", 100.0, 59.0, 17.1, 19.2, 18.9, 12.1, 3900),
        Pomiary(3, 3, "2023-06-25", "G12", 100.0, 72.0, 19.1, 19.2, 19.3, 19.4, 4000),
        Pomiary(4, 4, "2023-06-25", "G12", 100.0, 60.0, 19.1, 19.2, 19.3, 19.4, 5000)
    ]

    return osoby, liczniki, pracownicy, pomiary


def command_line_create_osoba():
    try:
        create_osoba(
            int(input("Id: ")),
            input("Imie: "),
            input("Nazwisko: "),
            input("Email: ")
        )

        print("Dodano osobe")
    except sqlite3.Error as er:
        print("Nie udało się dodac osoby:", er)


def command_line_create_pracownik():
    try:
        create_pracownik(
            int(input("Id: ")),
            input("Imie: "),
            input("Nazwisko: "),
            input("Adres: ")
        )
    except sqlite3.Error as er:
        print("Nie udało się dodac pracownika:", er)


def command_line_create_licznik():
    try:
        create_licznik(
            int(input("Id: ")),
            int(input("Id osoby: ")),
            input("Adres: ")
        )
    except sqlite3.Error as er:
        print("Nie udało się dodac licznika:", er)


def command_line_create_pomiar():
    try:
        create_pomiar(
            int(input("Id licznika: ")),
            int(input("Id pracownika: ")),
            input("Data: "),
            input("Taryfa: "),
            float(input("Energia czynna: ")),
            float(input("Energia oddana: ")),
            float(input("Energia Q1: ")),
            float(input("Energia Q2: ")),
            float(input("Energia Q3: ")),
            float(input("Energia Q4: ")),
            float(input("Maksymalna moc: "))
        )
    except sqlite3.Error as er:
        print("Nie udało się dodac pomiaru:", er)


def command_line_example_data():
    osoby, liczniki, pracownicy, pomiary = generate_example_data()
    try:
        store_all(osoby, liczniki, pracownicy, pomiary)
    except sqlite3.Error as er:
        print("Nie udało się zapisac przykładowych danych:", er)


def command_line_export_to_csv():
    try:
        export_all_to_csv()
    except sqlite3.Error as er:
        print("Nie udało się wyeksportowac danych do pliku csv:", er)