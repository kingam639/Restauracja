
class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena
    def __str__(self):
        return f"{self.nazwa} kosztuje {self.cena} zl"
# TODO: Nie wiem, czy powinnam tu robic nowe klasy Napoj i Jedzenie, ktore dziedzicza z klasy Produkt,
#  czy sama klasa Produkt wystarczy
class Napoj(Produkt):
    def __init__(self, nazwa, cena):
        super().__init__(nazwa, cena)
class Jedzenie(Produkt):
    def __init__(self, nazwa, cena):
        super().__init__(nazwa, cena)
class Konto:
    def __init__(self, konto):
        self.konto = konto
    def stan_konta(self, rachunek):
        self.konto += rachunek
class Restauracja:
    def __init__(self):
        # TODO czy tu sa potrzebne dwa osobne menu????
        self.menu_dan = {} # TODO a moze pusty {}?
        self.menu_napojow = {}
        # TODO czy moge to tak zrobic?????
        self.menu = [self.menu_dan, self.menu_napojow]
        self.zamowienie = []
        # TODO czy tutaj ma byc ta suma zliczana????
        self.suma = 0

    # TODO: uzywam jedzenia i napoju pozniej znowu, czy w takim razie powinnam stworzyc je tu?????
    # TODO: czy tworzyc osobna funkcje do menu dan i napojow?????
    def stworz_menu_dan(self, jedzenie):
        self.menu_dan[jedzenie.nazwa] = jedzenie.cena
    def stworz_menu_napojow(self, napoj):
        self.menu_napojow[napoj.nazwa] = napoj.cena
    def wyswietl_menu(self):
        for produkt in self.menu:
            print(produkt)
        # print(self.menu)
    def wyswietl_menu_dan(self):
        for danie in self.menu_dan:
            print(danie)
    def wyswietl_menu_napojow(self):
        for napoj in self.menu_napojow:
            print(napoj)
        # print(self.menu_napojow)
    def zloz_zamowienie(self, wybor):
        # TODO czy mam tu dac cala logike instrukcji, czy wywalic to poza klase??? - do przemyslenia, chyba jednak poza
        wybrany_produkt = False
        while not wybrany_produkt:
            if wybor in self.menu_dan or wybor in self.menu_napojow:
                self.zamowienie.append(wybor)
            elif wybor == "nie":
                # TODO czy moge tu dac return False???
                return False
            else:
                print("Nie ma takiego produktu")
    def wyswietl_zamowienie(self):
        for wybor in self.zamowienie:
            print(wybor)
    # czy
    def podlicz_zamowienie(self):
        for cena in self.zamowienie:
            self.suma += cena
frytki = Produkt("frytki", 7)
nuggetsy = Jedzenie("nuggetsy", 3)
macweg = Jedzenie("macweg", 15)
burger_drwala = Jedzenie("burger drwala", 30)
tortilla = Jedzenie("tortilla", 7)
macwrap = Jedzenie("mac wrap", 12)
sprite = Napoj("sprite", 5)
cola = Napoj("cola", 5)
restauracja = Restauracja()
# menu[frytki.nazwa] = frytki.cena
# menu[nuggetsy.nazwa] = nuggetsy.cena
# TODO czy moge tu stowrzyc liste produktow, ktore pozniej dam do petli for, zeby stworzyc menu?????
dania = [frytki, nuggetsy, macweg, burger_drwala, tortilla, macwrap]
napoje = [sprite, cola]
for danie in dania:
    restauracja.stworz_menu_dan(danie)
for napoj in napoje:
    restauracja.stworz_menu_napojow(napoj)
# menu.stworz_menu((nuggetsy.nazwa, nuggetsy.cena))
restauracja.wyswietl_menu()
restauracja.wyswietl_menu_dan()
restauracja.wyswietl_menu_napojow()
# skladanie zamowienia:
print("Aby zlozyc zamowienie, wybierz produkt z menu. Jesli jednak chcesz zakonczyc zamowienie, wpisz 'nie': ")
print("Zamawiam: ")
wybor = input().lower()
restauracja.zloz_zamowienie(wybor)





# Podchodzi klient do kasy, zamawia macwegi, sposrod kilku szpejow, i to robimy printami i inputami
# chemy proces zamawiania, platnosc wydanie produktu (obiekt tworzymy)
# zapytac o napoje
# menu ma wyswietlac kanapki i drinki, jesli nie podal drinkow ma sie go o nie zapytac, a jesli podal to zlicza
# zamowienie ma byc zrobione po mojemu
# mvp
# wypisanie menu
# menu_dan = {"nuggetsy": 3, "frytki": 5, "macweg": 6, "burger drwala": 30, "tortilla": 7, "mac wrap": 8}
# menu_drinkow = {"cola": 5, "sprite": 5}
# menu = {"menu_dan": menu_dan, "menu_drinkow": menu_drinkow}
# for typ_menu in menu:
#     print(typ_menu)
#     if "nuggetsy" in typ_menu:
#         print("a")
#
#
# print("Wybierz produkt z dostepnych: ")
# for element in menu.values():
#     for produkt, cena in element.items():
#         print(f"{produkt} kosztuje {cena} zl.")
# zamowienie_lista = []
# print("Aby zlozyc zamowienie, wybierz produkt z menu. Jesli jednak chcesz zakonczyc zamowienie, wpisz 'nie': ")
#
# wybrany_produkt = False
#
# while not wybrany_produkt:
#
#     wybor = input("Zamawiam: ")
#     for element in menu.values():
#         print(element)
#         if wybor in element:
#             print("c")
#             zamowienie_lista.append(wybor)
#             break
#     if wybor == "nie":
#         wybrany_produkt = True
#     else:
#         print("Nie ma takiego produktu")
# print(zamowienie_lista)

# czy_zamowil_drinki = []
# for produkt in zamowienie_lista:
#     if produkt in menu["menu_drinkow"]:
#         czy_zamowil_drinki.append(produkt)
# if not czy_zamowil_drinki:
#     print("A cos do picia podac?")
#     wybrany_produkt = False
#     while not wybrany_produkt:
#         wybor = input("Zamawiam: ")
#         if wybor in menu["menu_drinkow"]:
#             zamowienie_lista.append(wybor)
#             break  # albo chyba return - spr to! - tzn gdyby byla f., bo teraz je wywalilam
#         elif wybor == "nie":
#             wybrany_produkt = True
#         else:
#             print("Nie ma takiego produktu")
# print(zamowienie_lista)
# wartosc_zamowienia = 0
# for typ_menu in menu.values():
#     for element in zamowienie_lista:
#         if element in typ_menu:
#             wartosc_zamowienia += typ_menu[element]
# print(wartosc_zamowienia)
# # platnosc karta (stan konta klienta i maca, klient -, mac +)
# konto_klienta = 300
# konto_maca = 40000
# konto_klienta -= wartosc_zamowienia
# konto_maca += wartosc_zamowienia
# print(f"Na koncie masz: {konto_klienta}")
# print(f"Konto maca to: {konto_maca}")
# # wydanie produktu print wydano 9 nugetsow
# print(f"Wydano {", ".join(zamowienie_lista)}")

