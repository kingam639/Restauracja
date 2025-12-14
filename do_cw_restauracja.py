menu_dan = {"nuggetsy": 3, "frytki": 5, "macweg": 6, "burger drwala": 30, "tortilla": 7, "mac wrap": 8}
menu_drinkow = {"cola": 5, "sprite": 5}
menu = [menu_dan, menu_drinkow]
def wybierz_cos(menu, wybor):
    "Jesli uzytkownik nie wybral nic do picia, moze teraz zamowic napoj."
    if wybor in menu:
        return wybor
    elif wybor.lower() == "nie":
        return False
    else:
        return "Nie ma takiego produktu. Popraw swoje zamowienie."
# TODO 2: Zlozenie zamowienia przez klienta
wybor = input("Aby zlozyc zamowienie, wybierz produkt z menu. Jesli jednak chcesz zakonczyc zamowienie, wpisz 'nie': ")
for rodzaj_menu in menu:
    wybrany_produkt = wybierz_cos(rodzaj_menu, wybor)
# wybrany_produkt = wybierz_produkt(menu, wybor)
while wybrany_produkt:
    zamowienie.dodaj_do_koszyka(wybrany_produkt)
    print("Zamowienie ma obecnie wartosc:", zamowienie.wartosc_zamowienia)
    wybor = input(
        "Aby zlozyc zamowienie, wybierz produkt z menu. Jesli jednak chcesz zakonczyc zamowienie, wpisz 'nie': ")
