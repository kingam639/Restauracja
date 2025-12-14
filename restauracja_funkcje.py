# Podchodzi klient do kasy, zamawia macwegi, sposrod kilku szpejow, i to robimy printami i inputami
# chemy proces zamawiania, platnosc wydanie produktu (obiekt tworzymy)

# mvp
def wyswietl_menu(menu):
    """Funkcja wyswietla menu restauracji."""
    for produkt, cena in menu.items():
        print(f"{produkt} kosztuje {cena} zl.")

def zbierz_zamowienie(menu):
    """Funkcja zbiera zamowienie od klienta."""
    print("Aby zlozyc zamowienie, wybierz produkt z menu. Jesli jednak chcesz zakonczyc zamowienie, wpisz 'nie': ")
    wybrane_produkty = False
    zamowienie = [] # ta lista jest tworzona wewnatrz funkcji, dlatego trzeba ja zwrocic

    while not wybrane_produkty: # while True
        nazwa_produktu = input("Zamawiam: ")
        if nazwa_produktu in menu:
            dodaj_produkty(nazwa_produktu, zamowienie)
        elif nazwa_produktu == "nie":
            wybrane_produkty = True
        else:
            print("Nie ma takiego produktu. Popraw swoje zamowienie.")
    return zamowienie

def dodaj_produkty(nazwa, zamowienie):
    """Funkcja tworzy liste zamowionych przez klienta produktow."""
    zamowienie.append(nazwa)
    # tu nie trzeba zwracac listy, bo listy sa modyfikowalne w miejscu,

def oblicz_rachunek(zamowienie, menu):
    """Funkcja oblicza rachunek klienta - iteruje po zamowieniu i przekazuje ceny za produkty z menu."""
    suma = 0
    for element in zamowienie:
        suma += menu[element]
    return suma
#
# def saldo_konta(wysokosc_rachunku, konto):
#     """Funkcja aktualizuje stan konta restauracji i klienta po zlozeniu zamowienia przez klienta."""
#     saldo = konto + wysokosc_rachunku
#     return saldo

def wykonaj_platnosc(wysokosc_rachunku, od, do):
    if od > wysokosc_rachunku:
        od -= wysokosc_rachunku
        do += wysokosc_rachunku
    else:
        raise Exception()

def wydanie_produktow(zamowienie):
    """Funkcja wyswietla zamowienie zlozone przez klienta."""
    if not zamowienie:
        print("Nic nie zamowiles.")
    else:
        print("Wydano: ")
        for produkt in zamowienie:
            print(produkt)

# glowna funkcja

def main():

    menu = {"nuggetsy": 3, "frytki": 5, "macweg": 6, "burger drwala": 30, "tortilla": 7, "mac wrap": 8}
    konto_klienta = 300
    konto_restauracji = 40000

    # TODO: 1 Wyswietlenie menu
    wyswietl_menu(menu)

    # TODO 2: Zlozenie zamowienia przez klienta
    zamowienie_klienta = zbierz_zamowienie(menu)

    # TODO 3: Obliczenie rachunku klienta
    do_zaplaty = oblicz_rachunek(zamowienie_klienta, menu)
    print(f"Wysokosc twojego rachunku to: {do_zaplaty}")

    # TODO 4: Podanie aktualnego stanu konta klienta i restauracji
    # wstawilam "-" przed zmienna do zaplaty, bo chce odjac od salda wartosc zamowienia w saldzie klienta
    wykonaj_platnosc(do_zaplaty, konto_klienta, konto_restauracji)
    saldo_klienta = saldo_konta(-do_zaplaty , konto_klienta)
    saldo_restauracji = saldo_konta(do_zaplaty, konto_restauracji)
    print(f"Na Twoim koncie jest teraz {saldo_klienta} zl.")
    print(f"Na koncie restauracji jest teraz {saldo_restauracji} zl.")

    # TODO 5: Wydanie zamowienia klientowi
    wydanie_produktow(zamowienie_klienta)

main()





