# bo moge stworzyc funkcje czy_jest_ksiazka, ktora wlasnie sprawdza,
# czy ksiakza istnieje, ale no wlasnie, jesli nie istnieje to zwroci None
# i teraz w funkcji wypozycz_ksiazki - tej glownej moglabym zrobic flage koniec_wypozyczania i dac na False,
# czyli while not koniec_wypozyczania dalabym wybor = input(("Którą książkę wypożyczasz?, "
# "Wpisz koniec, jesli nie chcesz wiecej wypozyczac"))  wywolalabym te f. wybor = czy_jest ksiazka i i wtedy

ksiazki = {
    "hobbit": "fantasy",
    "diuna": "scifi",
    "fundacja": "scifi",
    "wiedźmin": "fantasy",
}

wypozyczenia = []  # Tu zapiszesz, co użytkownik wypożyczył

def wyswietl_ksiazki(ksiazki):
    for ksiazka, gatunek in ksiazki.items():
        print(f"Ksiazka {ksiazka} nalezy do gatunku {gatunek}.")

def czy_jest_ksiazka(ksiazki, wybor=None):
    if wybor in ksiazki:
        return wybor
    return None

def wypozycz_ksiazki(ksiazki):
    while True:
        wybor = input("Którą książkę wypożyczasz? Jesli nie chcesz wypozyczac ksiazki, wpisz 'koniec': ")
        if wybor == "koniec":
            break
        else:
            wybor2 = czy_jest_ksiazka(ksiazki, wybor)
            if wybor2:
                wypozyczenia.append(wybor2)
            else:
                print("Nie mamy takiej książki.")


def wyswietl_wypozyczone(wypozyczenia):
    for ksiazka in wypozyczenia:
        print(ksiazka)

wyswietl_ksiazki(ksiazki)
wypozycz_ksiazki(ksiazki)
wyswietl_wypozyczone(wypozyczenia)