# def oblicz_wysokosc_zamowienia(menu, zamowienie):
#     """Oblicza, ile musi zaplacic klient."""
#     wartosc_zamowienia = 0
#     for rodzaj_menu in menu:
#         for produkt in zamowienie:
#             if produkt in rodzaj_menu:
#                 wartosc_zamowienia += rodzaj_menu[produkt]
#     return wartosc_zamowienia

def wprowadz_nominaly():
    nominaly_klienta = {}
    nominal = input("Podaj nominal, ktory chcesz wplacic (wpisz nie, by skonczyc): ")
    while nominal != "nie":
        ilosc = int(input("Podaj ilosc banknotow tego nominalu: "))
        nominaly_klienta[nominal] = ilosc
        nominal = input("Podaj nominal, ktory chcesz wplacic (wpisz nie, by skonczyc): ")
    return nominaly_klienta

def wybierz_sposob_platnosci():
    """Pyta uzytkownika o sposob platnosci i bierze gotowke/karte."""
    forma_platnosci = input("Placisz karta, czy gotowka: ").lower()
    if forma_platnosci == "karta":
        print("Przybliz karte.")
    else:
        return wprowadz_nominaly()
        # print("Dziekuje za gotowke.")
    # return forma_platnosci

def oplac_zamowienie():
    forma_platnosci = input("Placisz karta, czy gotowka: ").lower()
    if forma_platnosci == "karta":
        print("Przybliz karte.")
    else:
        return wprowadz_nominaly()

# def wykonaj_platnosc(wysokosc_rachunku, od, do):
#     """Sprawdza, czy uzytkownik ma wystarczajaca kwote na koncie/odliczyl wlasciwa kwote, by zaplacic za zamowienie.
#     Jesli ma, rozlicza naleznosc miedzy klientem i maciem"""
#     if od > wysokosc_rachunku:
#         od -= wysokosc_rachunku
#         do += wysokosc_rachunku
#         return od, do
#     else:
#         raise Exception()

# def wyswietl_status_platnosci(forma_platnosci, u_klienta, w_macu):
#     """Wyswietla stan konta maca i klienta, jesli ten zaplacil karta. Jesli placil gotowka, wydaje reszte"""
#     if forma_platnosci == "gotowka":
#         print(f"Reszta to: {u_klienta}")
#     else:
#         print(f"Na koncie masz: {u_klienta} zl.")
#     print(f"Na koncie maca jest: {w_macu} zl.")