class Osoba:
    def __init__(self, id, imie, nazwisko, email):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email


class Licznik:
    def __init__(self, id, id_osoby, adres):
        self.id = id
        self.id_osoby = id_osoby
        self.adres = adres


class Pomiary:
    def __init__(self, id_licznika, id_pracownika, data, taryfa, energia_czynna, energia_oddana, energia_q1, energia_q2, energia_q3, energia_q4, maks_moc):
        self.id_licznika = id_licznika
        self.id_pracownika = id_pracownika
        self.data = data
        self.taryfa = taryfa
        self.energia_czynna = energia_czynna
        self.energia_oddana = energia_oddana
        self.energia_q1 = energia_q1
        self.energia_q2 = energia_q2
        self.energia_q3 = energia_q3
        self.energia_q4 = energia_q4
        self.maks_moc = maks_moc


class Pracownik:
    def __init__(self, id, imie, nazwisko, miejsce_zatrudnienia):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.miejsce_zatrudnienia = miejsce_zatrudnienia