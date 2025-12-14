from platnosc import wybierz_sposob_platnosci, wykonaj_platnosc, wyswietl_status_platnosci

class Zamowienie:
    def __init__(self, menu):
        self.koszyk = []
        self.wartosc_zamowienia = 0
        self.menu = menu

    def dodaj_do_koszyka(self, produkt):
        self.koszyk.append(produkt)
        self.oblicz_wysokosc_zamowienia()

    def oblicz_wysokosc_zamowienia(self):
        """Oblicza, ile musi zaplacic klient."""
        self.wartosc_zamowienia = 0
        for rodzaj_menu in self.menu:
            for produkt in self.koszyk:
                if produkt in rodzaj_menu:
                    self.wartosc_zamowienia += rodzaj_menu[produkt]

    def oplac_zamowienie(self):
        konto_klienta = 300
        konto_maca = 20000
        print("Do zaplaty masz:", self.wartosc_zamowienia)
        sposob_platnosci = wybierz_sposob_platnosci()
        # TODO 6: Rozliczenie zakupu
        rozliczenie_klienta, rozliczenie_maca = (
            wykonaj_platnosc(self.wartosc_zamowienia, konto_klienta, konto_maca))
        wyswietl_status_platnosci(sposob_platnosci, rozliczenie_klienta, rozliczenie_maca)