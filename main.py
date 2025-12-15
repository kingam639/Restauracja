from zamowienie import Zamowienie
from zbieranie_zamowienia import wyswietl_pelne_menu, wybierz_produkt, zbierz_zamowienie, czy_zamowil_napoj
from platnosc import wybierz_sposob_platnosci
from kasa import Kasa

menu_dan = {"nuggetsy": 3, "frytki": 5, "macweg": 6, "burger drwala": 30, "tortilla": 7, "mac wrap": 8}
menu_drinkow = {"cola": 5, "sprite": 5}
menu = [menu_dan, menu_drinkow]
nominaly_restauracji = {"50": 5, "20": 4, "10": 8, "5": 7, "2": 10}
nominaly_klienta = {"10": 3, "5": 4}

zamowienie = Zamowienie(menu)
kasa = Kasa(nominaly_restauracji)
kasa.oblicz_stan_konta()
# TODO: 1 Wyswietlenie menu
wyswietl_pelne_menu(menu)
# TODO 2: Zlozenie zamowienia przez klienta
# wybrany_produkt = True
# while wybrany_produkt:
wybrany_produkt = zbierz_zamowienie(menu, zamowienie)
# zamowienie.dodaj_do_koszyka(wybrany_produkt)
# print("Aby zlozyc zamowienie, wybierz produkt z menu. Jesli jednak chcesz zakonczyc zamowienie, wpisz 'nie'.")
# wybrany_produkt = True
# while wybrany_produkt:
#     wybor = input("Zamawiam: ")
#     for rodzaj_menu in menu:
#         wybrany_produkt = wybierz_cos(rodzaj_menu, wybor)
#         if wybrany_produkt:
#             zamowienie.dodaj_do_koszyka(wybrany_produkt)
#             print("Zamowienie ma obecnie wartosc:", zamowienie.wartosc_zamowienia)
#             break
#         elif wybrany_produkt == False:
#             break
#     else:
#         print("Nie ma takiego produktu.")
#         wybrany_produkt = True
# TODO 3: Pytanie uzytkownika o napoj, jesli go nie zamowil
# if not czy_zamowil_napoj(menu_drinkow, zamowienie.koszyk):
#     # wybrany_napoj = False
#     print("A cos do picia podac?")
#     wybor = input("Zamawiam: ")
#     wybrany_napoj = wybierz_produkt(menu_drinkow, wybor)
#     while wybrany_napoj:
#         zamowienie.dodaj_do_koszyka(wybrany_napoj)
#         print("Zamowienie ma obecnie wartosc:", zamowienie.wartosc_zamowienia)
#         wybor = input("Zamawiam: ")
#         wybrany_napoj = wybierz_produkt(menu_drinkow, wybor)
# print(f"Koszt Twojego zamowienia to: {zamowienie.wartosc_zamowienia}")

if not czy_zamowil_napoj(menu_drinkow, zamowienie.koszyk):
    print("A cos do picia podac?")
    wybor = input("Co wybierasz? (nie aby zakończyć) ")

    while wybor != "nie":
        wybrany_napoj = wybierz_produkt(menu_drinkow, wybor)

        if wybrany_napoj:
            zamowienie.dodaj_do_koszyka(wybrany_napoj)
            print("Zamowienie ma obecnie wartosc:", zamowienie.wartosc_zamowienia)
        else:
            print("Nie ma takiego produktu")

        wybor = input("Co wybierasz? (nie aby zakończyć) ")
            # wybrany_napoj = wybierz_produkt(menu_drinkow, wybor)
print(f"Koszt Twojego zamowienia to: {zamowienie.wartosc_zamowienia}")

# zamowienie.oplac_zamowienie()


# print(kasa.stan_konta)
# wplata = kasa.przelicz_banknoty_klienta(nominaly_klienta)
nominaly_klienta = wybierz_sposob_platnosci()
kasa.przyjmij_zaplate(zamowienie, nominaly_klienta)
reszta = kasa.oblicz_reszte(zamowienie, nominaly_klienta)
kasa.wydaj_reszte(reszta)
print(kasa.stan_konta)