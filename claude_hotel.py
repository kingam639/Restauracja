# Zadanie 4: System rezerwacji hotelu (trudniejsze!)
# Opis:
# Hotel ma pokoje w różnych kategoriach. Goście mogą rezerwować pokoje na określoną liczbę dni.
# Co program ma robić:
# Wyświetlić wszystkie dostępne pokoje (numer i cena za dobę)
# Pytać gościa: "Który pokój rezerwujesz?" (póki nie wpisze "koniec")
# NOWE: Dla każdego pokoju zapytać: "Na ile dni?" (liczba całkowita)
# Jeśli pokój istnieje → dodać do rezerwacji jako krotkę (numer_pokoju, liczba_dni)
# Jeśli nie istnieje → "Nie mamy takiego pokoju"
# Na końcu wyświetlić:
# Wszystkie rezerwacje (pokój + liczba dni)
# Koszt każdej rezerwacji (cena_za_dobe * liczba_dni)
# Całkowity koszt wszystkich rezerwacji
# 3. Teraz wywołujesz funkcję liczącą:
#    └─> oblicz_i_pokaz_koszty(rezerwacje, hotel)
#        └─> dla każdej rezerwacji:
#            └─> znajdź cenę pokoju
#            └─> pomnóż przez dni
#            └─> wypisz

ekonomiczne = {
    "pokoj_101": 100,  # cena za dobę
    "pokoj_102": 100,
    "pokoj_103": 120,
}

luksusowe = {
    "pokoj_201": 300,
    "pokoj_202": 350,
}

hotel = [ekonomiczne, luksusowe]

rezerwacje = []  # Lista krotek: (numer_pokoju, liczba_dni)

def wyswietl_pokoje_z_kategorii(typ_pokoju):
    """Wyświetla pokoje z jednej kategorii (ekonomiczne lub luksusowe)."""
    for pokoj, cena in typ_pokoju.items():
        print(f"{pokoj} kosztuje {cena} zl za dobe.")

def wyswietl_wszystkie_pokoje(hotel):
    """Wyświetla wszystkie pokoje ze wszystkich kategorii."""
    for pokoje in hotel:
        wyswietl_pokoje_z_kategorii(pokoje)

def sprawdz_w_kategorii(pokoje, pokoj=None):
    """Sprawdza czy pokój istnieje w danej kategorii."""
    if pokoj in pokoje:
        return True
    return False

def sprawdz_w_hotelu(hotel, pokoj=None):
    """Sprawdza czy pokój istnieje w całym hotelu (we wszystkich kategoriach)."""
    if not pokoj:
        # jesli argument funkcji pokoj=None, to wtedy: if not None == True, czyli zada pytanie o pokoj
        pokoj = input("Ktory pokoj rezerwujesz? ")
    for typy_pokoi in hotel:
        if sprawdz_w_kategorii(typy_pokoi, pokoj):
            return True
    return False

def rezerwuj_pokoj(hotel):
    """Zbiera rezerwacje od gościa. Kończy się gdy gość wpisze 'koniec'."""
    while True:
        numer_pokoju = input("Ktory pokoj rezerwujesz? ")
        if numer_pokoju == "koniec":
            break
        elif sprawdz_w_hotelu(hotel, numer_pokoju):
            liczba_dni = int(input("Na ile dni? "))
            rezerwacje.append((numer_pokoju, liczba_dni))
        else:
            print("Nie mamy takiego pokoju.")

def wyswietl_rezerwacje(rezerwacje):
    """Wyświetla listę wszystkich dokonanych rezerwacji."""
    for pokoj, dni in rezerwacje:
        print(f"Zarezerwowales pokoj {pokoj} na {dni} dni.")

def oblicz_koszt_rezerwacji(pokoj, dni, hotel):
    """Oblicza koszt jednej rezerwacji (cena pokoju * liczba dni)."""
    for typ_pokoju in hotel:
        if pokoj in typ_pokoju:
            cena = typ_pokoju[pokoj] * dni
            return cena
    return 0 # jeśli pokoju nie ma

def oblicz_calkowity_koszt(rezerwacje, hotel):
    """Oblicza łączny koszt wszystkich rezerwacji."""
    suma = 0
    for pokoj, dni in rezerwacje:
        koszt = oblicz_koszt_rezerwacji(pokoj, dni, hotel)
        suma += koszt
    return suma

def wyswietl_koszty(rezerwacje, hotel):
    """Wyświetla koszt każdej rezerwacji i łączny koszt."""
    for pokoj, dni in rezerwacje:
        koszt = oblicz_koszt_rezerwacji(pokoj, dni, hotel)
        print(f"Koszt rezerwacji pokoju {pokoj} to {koszt} zl.")

    calkowity_koszt = oblicz_calkowity_koszt(rezerwacje, hotel)
    print(f"Calkowity koszt rezerwacji to {calkowity_koszt} zl.")


wyswietl_wszystkie_pokoje(hotel)
rezerwuj_pokoj(hotel)
wyswietl_rezerwacje(rezerwacje)
wyswietl_koszty(rezerwacje, hotel)

#
#
