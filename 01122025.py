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
            continue # wraca na poczatek petli
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