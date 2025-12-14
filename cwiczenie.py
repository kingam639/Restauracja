# Podchodzi klient do kasy, zamawia macwegi, sposrod kilku szpejow, i to robimy printami i inputami
# chemy proces zamawiania, platnosc wydanie produktu (obiekt tworzymy)
# zapytac o napoje
# menu ma wyswietlac kanapki i drinki, jesli nie podal drinkow ma sie go o nie zapytac, a jesli podal to zlicza
# zamowienie ma byc zrobione po mojemu
# mvp
# wypisanie menu

def wyswietl_menu(menu):
    for produkt, cena in menu.items():
        print(f"{produkt} kosztuje {cena} zl.")
def wyswietl_pelne_menu(menu):
    print("Pełne menu:")
    for element in menu:
        wyswietl_menu(element)
menu_dan = {"nuggetsy": 3, "frytki": 5, "macweg": 6, "burger drwala": 30, "tortilla": 7, "mac wrap": 8}
menu_drinkow = {"cola": 5, "sprite": 5}
menu = [menu_dan, menu_drinkow]
# def wybierz_produkt(menu, wybor):
#     """Uzytkownik sklada zamowienie."""
#     # czy_zamawia = True
#     # while czy_zamawia:
#     for rodzaj_menu in menu:
#         wynik = wybierz_cos(rodzaj_menu, wybor)
#         if wynik == False:
#             return wynik
#         elif wynik == "Nie ma takiego produktu. Popraw swoje zamowienie.":
#             continue
#         else:
#             return wybor
#     else:
#         print("Nie ma takiego produktu. Popraw swoje zamowienie.")
def wybierz_cos(menu, wybor):
    "Sprawdza, co wybral klient."
    if wybor in menu:
        return wybor
    elif wybor.lower() == "nie":
        return False
    # else:
    #     return "Nie ma takiego produktu. Popraw swoje zamowienie."


# wybrany_produkt = wybierz_produkt(menu)
# while wybrany_produkt:
#     zamowienie.dodaj_do_koszyka(wybrany_produkt)
#     print("Zamowienie ma obecnie wartosc:", zamowienie.wartosc_zamowienia)
#     wybrany_produkt = wybierz_produkt(menu)
        # return wybierz_cos(menu)
def czy_zamowil_napoj(menu, zamowienie):
    """Sprawdza, czy uzytkownik zamowil napoj i zwraca True, jesli to zrobil."""
    for produkt in zamowienie:
        if produkt in menu:
            return True
    # TODO gdybym nie dala tu return False, zwrocilby niejawnie None, a w instrukcji if not czy_zamowil_napoj
    #  not None i not False ewaluuja do True, tylko pytanie, ktore jest lepsze?
    return False
def oblicz_wysokosc_zamowienia(menu, zamowienie):
    """Oblicza, ile musi zaplacic klient."""
    wartosc_zamowienia = 0
    for rodzaj_menu in menu:
        for produkt in zamowienie:
            if produkt in rodzaj_menu:
                wartosc_zamowienia += rodzaj_menu[produkt]
    return wartosc_zamowienia

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
            wykonaj_platnosc(zamowienie.wartosc_zamowienia, konto_klienta, konto_maca))
        wyswietl_status_platnosci(sposob_platnosci, rozliczenie_klienta, rozliczenie_maca)

def wybierz_sposob_platnosci():
    """Pyta uzytkownika o sposob platnosci i bierze gotowke/karte."""
    forma_platnosci = input("Placisz karta, czy gotowka: ").lower()
    if forma_platnosci == "karta":
        print("Przybliz karte.")
    else:
        print("Dziekuje za gotowke.")
    return forma_platnosci
def wykonaj_platnosc(wysokosc_rachunku, od, do):
    """Sprawdza, czy uzytkownik ma wystarczajaca kwote na koncie/odliczyl wlasciwa kwote, by zaplacic za zamowienie.
    Jesli ma, rozlicza naleznosc miedzy klientem i maciem"""
    if od > wysokosc_rachunku:
        od -= wysokosc_rachunku
        do += wysokosc_rachunku
        return od, do
    else:
        raise Exception()
def wyswietl_status_platnosci(forma_platnosci, u_klienta, w_macu):
    """Wyswietla stan konta maca i klienta, jesli ten zaplacil karta. Jesli placil gotowka, wydaje reszte"""
    if forma_platnosci == "gotowka":
        print(f"Reszta to: {u_klienta}")
    else:
        print(f"Na koncie masz: {u_klienta} zl.")
    print(f"Na koncie maca jest: {w_macu} zl.")
zamowienie = Zamowienie(menu)
# TODO: 1 Wyswietlenie menu
wyswietl_pelne_menu(menu)
# TODO 2: Zlozenie zamowienia przez klienta
print("Aby zlozyc zamowienie, wybierz produkt z menu. Jesli jednak chcesz zakonczyc zamowienie, wpisz 'nie': ")
wybrany_produkt = True
while wybrany_produkt:
    wybor = input(
        "Aby zlozyc zamowienie, wybierz produkt z menu. Jesli jednak chcesz zakonczyc zamowienie, wpisz 'nie': ")
    for rodzaj_menu in menu:
        wybrany_produkt = wybierz_cos(rodzaj_menu, wybor)
        if wybrany_produkt:
            zamowienie.dodaj_do_koszyka(wybrany_produkt)
            print("Zamowienie ma obecnie wartosc:", zamowienie.wartosc_zamowienia)
            break
        elif wybrany_produkt == False:
            break
    else:
        print("Nie ma takiego produktu.")
# TODO 3: Pytanie uzytkownika o napoj, jesli go nie zamowil
if not czy_zamowil_napoj(menu_drinkow, zamowienie.koszyk):
    # wybrany_napoj = False
    print("A cos do picia podac?")
    wybor = input("Zamawiam: ")
    wybrany_napoj = wybierz_cos(menu_drinkow, wybor)
    while wybrany_napoj:
        zamowienie.dodaj_do_koszyka(wybrany_napoj)
        print("Zamowienie ma obecnie wartosc:", zamowienie.wartosc_zamowienia)
        wybor = input("Zamawiam: ")
        wybrany_napoj = wybierz_cos(menu_drinkow, wybor)

# if not czy_zamowil_napoj(menu_drinkow, zamowienie.koszyk):
#     wybrany_napoj = False
#     print("A cos do picia podac?")
#     wybor = input(
#         "Aby zlozyc zamowienie, wybierz produkt z menu. Jesli jednak chcesz zakonczyc zamowienie, wpisz 'nie': ")
#     wybrany_napoj = wybierz_cos(menu_drinkow, wybor)
#     while wybrany_napoj:
#         zamowienie.dodaj_do_koszyka(wybrany_napoj)
#         print("Zamowienie ma obecnie wartosc:", zamowienie.wartosc_zamowienia)
#         wybor = input(
#             "Aby zlozyc zamowienie, wybierz produkt z menu. Jesli jednak chcesz zakonczyc zamowienie, wpisz 'nie': ")
#         wybrany_napoj = wybierz_cos(menu_drinkow, wybor)
zamowienie.oplac_zamowienie()


menu_dan = {
    "nuggetsy": 3,
    "frytki": 5,
    "macweg": 6,
    "burger drwala": 30,
    "tortilla": 7,
    "mac wrap": 8,
}
menu_drinkow = {"cola": 5, "sprite": 5}
menu = [menu_dan, menu_drinkow]

liczba_klientow = 5

lista_list_zamowien = []


def wypisz_menu(menu):
    for podmenu in menu:
        wypisz_podmenu(podmenu)


def wypisz_podmenu(menu):
    for produkt in menu:
        print(produkt, menu[produkt], "zł")


# pojedyncze menu
def wybierz_produkt(menu, wybor=None):
    if not wybor:
        wybor = input("Co wybierasz? ")
    if wybor in menu:
        return wybor
    return None


# zagnieżdżone menu
def wybierz_cos(menu, wybor=None):
    if not wybor:
        wybor = input("Co wybierasz? ")
    for podmenu in menu:
        wybor2 = wybierz_produkt(podmenu, wybor)
        if wybor2:
            return wybor2
    return None


# zbierz zamowienie póki nie wpiszemy "nie"
def zbierz_zamowienie(menu):
    zamowienie = []
    while True:
        wybor = input("Co wybierasz? (nie aby zakończyć) ")
        if wybor == "nie":
            break
        wybor2 = wybierz_cos(menu, wybor)
        if not wybor2:
            print("Nie ma takiego produktu")
            continue
        zamowienie.append(wybor)
    lista_list_zamowien.append(zamowienie)


def wypisz_zamowienia(lista_list_zamowien):
    i = 1
    for lista_zamowien in lista_list_zamowien:
        print(i, lista_zamowien)
        i += 1


#
for i in range(liczba_klientow):
    wypisz_menu(menu)
    print("### Klient", i + 1, "###")
    zbierz_zamowienie(menu)
wypisz_zamowienia(lista_list_zamowien)


