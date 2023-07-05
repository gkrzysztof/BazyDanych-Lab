import csv


def export_pomiary_to_csv(pomiary):
    with open('../pomiary.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for pomiar in pomiary:
            writer.writerow([
                pomiar.id_licznika, pomiar.id_pracownika, pomiar.data,
                pomiar.taryfa, pomiar.energia_czynna, pomiar.energia_oddana,
                pomiar.energia_q1, pomiar.energia_q2, pomiar.energia_q3, pomiar.energia_q4, pomiar.maks_moc])


def export_liczniki_to_csv(liczniki):
    with open('../liczniki.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for licznik in liczniki:
            writer.writerow([licznik.id, licznik.id_osoby, licznik.adres])


def export_osoby_to_csv(osoby):
    with open('../osoby.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for osoba in osoby:
            writer.writerow([osoba.id, osoba.imie, osoba.nazwisko, osoba.email])


def export_pracownicy_csv(pracownicy):
    with open('../pracownicy.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for pracownik in pracownicy:
            writer.writerow([pracownik.id, pracownik.imie, pracownik.nazwisko, pracownik.miejsce_zatrudnienia])
