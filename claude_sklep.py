# Zadanie 3: Sklep internetowy z kategoriami
# Opis:
# Masz sklep z produktami podzielonymi na kategorie. Użytkownik może kupować rzeczy z różnych kategorii.
# Co program ma robić:
# Wyświetlić wszystkie produkty ze wszystkich kategorii (nazwa i cena)
# Pytać: "Co kupujesz?" (póki nie wpisze "koniec")
# Jeśli produkt istnieje (w którejkolwiek kategorii!) → dodać do koszyka i powiedzieć "Dodano do koszyka!"
# Jeśli nie istnieje → "Nie mamy takiego produktu"
# Na końcu wypisać koszyk i policzyć całkowitą cenę
elektronika = {
    "laptop": 3000,
    "mysz": 50,
    "klawiatura": 200,
}

odziez = {
    "koszulka": 80,
    "spodnie": 150,
    "kurtka": 400,
}

sklep = [elektronika, odziez]  # ← UWAGA: lista słowników!

koszyk = []  # Co użytkownik kupi

def wyswietl_produkty_z_kategorii(kategoria):
    """Wyswietla produkty z pojedynczych kategorii."""
    for produkt, cena in kategoria.items():
        print(f"{produkt} kosztuje {cena} zl.")

def wyswietl_caly_sklep(kategorie):
    """Wyswietla produkty z calego sklepu."""
    for kategoria in kategorie:
        wyswietl_produkty_z_kategorii(kategoria)

def czy_produkt_istnieje(kategoria, produkt=None):
    """Sprawdza, czy produkt istnieje w podanej kategorii."""
    if produkt in kategoria:
        return produkt
    return None

def znajdz_produkt_w_sklepie(kategorie, produkt=None):
    """Sprawdza, czy produkt jest w calym sklepie."""
    for kategoria in kategorie:
        # tu juz musze przekazac prawdziwy produkt, a nie None
        if czy_produkt_istnieje(kategoria, produkt): # == if produkt, bo funkcja
            return produkt

def zbierz_zamowienie(kategorie):
    """Zbiera cale zamowienie klienta. Gdy klient wpisze koniec zamawianie sie konczy."""
    while True:
        produkt = input("Co kupujesz? Wpisz koniec, by zakonczyc zakupy. ")
        if produkt == "koniec":
            break
        elif znajdz_produkt_w_sklepie(kategorie, produkt):
            koszyk.append(produkt)
            print("Dodano do koszyka.")
        else:
            print("Nie ma takiego produktu.")

def policz_cene(koszyk, kategorie):
    """Liczy calkowita cene zamowienia."""
    cena = 0
    for towar in koszyk:
        for kategoria in kategorie:
            if towar in kategoria:
                cena += kategoria[towar]
                break
    return cena

def wyswietl_zawartosc_koszyka(koszyk, sklep):
    """Wyswietla zawartosc koszyka."""
    print("W koszyku znajduja sie: ")
    for produkt in koszyk:
        print("*", produkt)
    cena = policz_cene(koszyk, sklep)
    print(f"Calkowity koszt zamowienia to {cena} zl.")

wyswietl_caly_sklep(sklep)
zbierz_zamowienie(sklep)
wyswietl_zawartosc_koszyka(koszyk, sklep)