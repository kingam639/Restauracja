# Zadanie 2: Ekwipunek w grze RPG
# Opis:
# Masz bohatera w grze, który zbiera przedmioty. Każdy przedmiot ma swoją rzadkość.
# Co program ma robić:
#
# Wyświetlić dostępne przedmioty (nazwa i rzadkość)
# Pytać gracza: "Co podnosisz?" (póki nie wpisze "wyjdz")
# Jeśli przedmiot istnieje → dodać do ekwipunku i powiedzieć "Podniesiono [nazwa]!"
# Jeśli nie istnieje → powiedzieć "Nie ma tu takiego przedmiotu"
# Na końcu wypisać cały ekwipunek

przedmioty_w_swiecie = {
    "miecz": "rzadki",
    "mikser": "legendarny",
    "zbroja": "zwykly",
    "eliksir": "rzadki",
    "zloto": "zwykly",
}

ekwipunek = []  # Co bohater zbierze

def wyswietl_przedmioty(przedmioty):
    """Wyświetla dostępne przedmioty (nazwa i rzadkość)."""
    for przedmiot, rzadkosc in przedmioty.items():
        print(f"{przedmiot} jest {rzadkosc}.")

def sprawdz_przedmiot(przedmioty,przedmiot=None):
    """Sprawdza, czy przedmiot istnieje."""
    if przedmiot in przedmioty:
        return przedmiot
    return None

def zbierz_ekwipunek(przedmioty):
    """Pyta gracza: "Co podnosisz?" (póki nie wpisze "wyjdz")
    Dodaje przedmiot do ekwipunku i wyswietla "Podniesiono [nazwa]!
    Jeśli nie istnieje → wyswietla "Nie ma tu takiego przedmiotu"""
    while True:
        przedmiot = input("Co podnosisz? Wpisz 'wyjdz', jesli chcesz zakonczyc: ")
        if przedmiot == "wyjdz":
            break
        if sprawdz_przedmiot(przedmioty_w_swiecie, przedmiot):
            ekwipunek.append(przedmiot)
        else:
            print("Nie ma tu takiego przedmiotu.")

def wyswietl_ekwipunek(ekwipunek):
    """Wypisuje cały ekwipunek."""
    for przedmiot in ekwipunek:
        print(przedmiot)

wyswietl_przedmioty(przedmioty_w_swiecie)
zbierz_ekwipunek(przedmioty_w_swiecie)
wyswietl_ekwipunek(ekwipunek)
