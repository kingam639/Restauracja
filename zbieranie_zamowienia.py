def wyswietl_menu(menu):
    for produkt, cena in menu.items():
        print(f"{produkt} kosztuje {cena} zl.")

def wyswietl_pelne_menu(menu):
    print("Pełne menu:")
    for element in menu:
        wyswietl_menu(element)

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
def zbierz_zamowienie(menu, zamowienie):
    while True:
        wybor = input("Co wybierasz? (nie aby zakończyć) ")
        if wybor == "nie":
            break
        wybor2 = wybierz_cos(menu, wybor)
        if not wybor2:
            print("Nie ma takiego produktu")
            continue # wraca na poczatek petli
        # to troche lipa
        zamowienie.dodaj_do_koszyka(wybor2)
        print("Zamowienie ma obecnie wartosc:", zamowienie.wartosc_zamowienia)

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
#
# def wybierz_cos(menu, wybor):
#     "Sprawdza, co wybral klient."
#     if wybor in menu:
#         return wybor
#     elif wybor.lower() == "nie":
#         return False
#     else:
#         print("Nie ma takiego produktu. Popraw swoje zamowienie.")
#
def czy_zamowil_napoj(menu, zamowienie):
    """Sprawdza, czy klient zamowil napoj i zwraca True, jesli to zrobil."""
    for produkt in zamowienie:
        if produkt in menu:
            return True
    # TODO gdybym nie dala tu return False, zwrocilby niejawnie None, a w instrukcji if not czy_zamowil_napoj
    #  not None i not False ewaluuja do True, tylko pytanie, ktore jest lepsze?
    return False