def wyswietl_menu(menu):
    for produkt, cena in menu.items():
        print(f"{produkt} kosztuje {cena} zl.")

def wyswietl_pelne_menu(menu):
    print("Pełne menu:")
    for element in menu:
        wyswietl_menu(element)

def wybierz_produkt(menu, wybor):
    """Uzytkownik sklada zamowienie."""
    # czy_zamawia = True
    # while czy_zamawia:
    for rodzaj_menu in menu:
        wynik = wybierz_cos(rodzaj_menu, wybor)
        if wynik == False:
            return wynik
        elif wynik == "Nie ma takiego produktu. Popraw swoje zamowienie.":
            continue
        else:
            return wybor
    else:
        print("Nie ma takiego produktu. Popraw swoje zamowienie.")

def wybierz_cos(menu, wybor):
    "Sprawdza, co wybral klient."
    if wybor in menu:
        return wybor
    elif wybor.lower() == "nie":
        return False
    else:
        print("Nie ma takiego produktu. Popraw swoje zamowienie.")

def czy_zamowil_napoj(menu, zamowienie):
    """Sprawdza, czy klient zamowil napoj i zwraca True, jesli to zrobil."""
    for produkt in zamowienie:
        if produkt in menu:
            return True
    # TODO gdybym nie dala tu return False, zwrocilby niejawnie None, a w instrukcji if not czy_zamowil_napoj
    #  not None i not False ewaluuja do True, tylko pytanie, ktore jest lepsze?
    return False