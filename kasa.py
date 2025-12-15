

nominaly_restauracji = {"50": 5, "20": 4, "10": 8, "5": 7, "2": 10}
nominaly_klienta = {"10": 3, "5": 4}


class Kasa:
    def __init__(self, nominaly):
        self.nominaly = nominaly
        self.stan_konta = 0 # nie wiem, czy to tak moze byc

    def oblicz_stan_konta(self):
        for nominal, wartosc in self.nominaly.items():
            self.stan_konta += wartosc * int(nominal)

    def przelicz_banknoty_klienta(self, nominaly_klienta):
        wplata = 0
        for nominal, ilosc in nominaly_klienta.items():
            wplata += ilosc * int(nominal)
        return wplata

    # def czy_klient_wplacil_dosc(self, nominaly_klienta, zamowienie): # to zgadywalam, musze spr dokladnie jak to dziala
    #     if self.przelicz_banknoty_klienta(nominaly_klienta) >= zamowienie.wartosc_zamowienia:
    #         return True
    #     return False
    def przyjmij_zaplate(self, zamowienie, nominaly_klienta):
        wplata = self.przelicz_banknoty_klienta(nominaly_klienta)
        roznica = wplata - zamowienie.wartosc_zamowienia
        if roznica >= 0:
            self.stan_konta += wplata
            # nominaly wplywaja do kasy
            for nominal, ilosc in nominaly_klienta.items():
                if nominal in self.nominaly:
                    self.nominaly[nominal] += ilosc # zwieksza ilosc nominalow, ktore sa w kasie
                else:
                    self.nominaly[nominal] = ilosc # tworzy nowe nominaly
        else:
            print(f"Wplaciles za malo o {abs(roznica)} zl.")

    def oblicz_reszte(self, zamowienie, nominaly_klienta):
        reszta = self.przelicz_banknoty_klienta(nominaly_klienta) - zamowienie.wartosc_zamowienia
        return reszta

    def wydaj_reszte(self, kwota_reszty):
        reszta = {}
        for nominal, ilosc in self.nominaly.items():
            while kwota_reszty > 0 and ilosc > 0:
                if int(nominal) <= kwota_reszty:
                    kwota_reszty -= int(nominal)
                    self.stan_konta -= int(nominal)
                    self.nominaly[nominal] -= 1
                    ilosc -= 1
                    # sprawdza, czy nominal jest juz w slowniku reszta
                    if nominal in reszta:
                        # jesli nominal jest w slowniku dodaje kolejny banknot
                        reszta[nominal] += 1
                    else:
                        # jesli nominalu nie ma slowniku tworzy ten nowy nominal
                        reszta[nominal] = 1
        if kwota_reszty == 0:
            print("Wydales cala reszte.")
            return reszta
        else:
            print(f"Przepraszam nie mam reszty {kwota_reszty}. ")

 # wyplata = self.oblicz_reszte(zamowienie, nominaly_klienta) ??? czy te funkcje wywoluje tu, czy wlasnie daje
# jako paramert kwota_reszty
# kasa = Kasa(nominaly_restauracji)
# kasa.oblicz_stan_konta()
# print(kasa.stan_konta)
# wplata = kasa.przelicz_banknoty_klienta(nominaly_klienta)
# print(wplata)


if __name__ == "__main__":
    # Ten kod wykona się TYLKO gdy uruchomisz kasa.py bezpośrednio
    # NIE wykona się gdy zaimportujesz Kasa gdzie indziej

    print("=== TEST KLASY KASA ===")
    nominaly_test = {"50": 5, "20": 4, "10": 8}
    kasa = Kasa(nominaly_test)
    kasa.oblicz_stan_konta()
    print(f"Stan konta: {kasa.stan_konta}")

    nominaly_klienta_test = {"10": 3, "5": 4}
    wplata = kasa.przelicz_banknoty_klienta(nominaly_klienta_test)
    print(f"Wpłata klienta: {wplata}")
