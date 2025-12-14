from zamowienie import Zamowienie
from zbieranie_zamowienia import wyswietl_pelne_menu, wybierz_cos, czy_zamowil_napoj


menu_dan = {"nuggetsy": 3, "frytki": 5, "macweg": 6, "burger drwala": 30, "tortilla": 7, "mac wrap": 8}
menu_drinkow = {"cola": 5, "sprite": 5}
menu = [menu_dan, menu_drinkow]

zamowienie = Zamowienie(menu)
# TODO: 1 Wyswietlenie menu
wyswietl_pelne_menu(menu)
# TODO 2: Zlozenie zamowienia przez klienta
print("Aby zlozyc zamowienie, wybierz produkt z menu. Jesli jednak chcesz zakonczyc zamowienie, wpisz 'nie'.")
wybrany_produkt = True
while wybrany_produkt:
    wybor = input("Zamawiam: ")
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
        wybrany_produkt = True
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
zamowienie.oplac_zamowienie()
