from zamowienie import Zamowienie


nominaly_restauracji = {"50": 5, "20": 4, "10": 8, "5": 7, "2": 10}


class Kasa:
    def __init__(self, nominaly):
        self.nominaly = nominaly
        # self.stan_konta = 0 # nie wiem, czy to tak moze byc
        self.stan_konta = self.oblicz_stan_konta() ### czy to tak moze byc????

    def oblicz_stan_konta(self):
        for wartosc in self.nominaly.values():
            self.stan_konta += wartosc

    def przelicz_banknoty_klienta(self, nominaly_klienta):
        wplata = 0
        for wartosc in nominaly_klienta.values():
            wplata += wartosc

    def czy_klient_wplacil_dosc(self, wplata, zamowienie): # to zgadywalam, musze spr dokladnie jak to dziala
        if wplata >= zamowienie.oblicz_wysokosc_zamowienia():
            return True
        return False

    def przyjmij_zaplate(self):
        if self.czy_klient_wplacil_dosc(wplata, zamowienie): # watpie ze to tak ma byc???
            self.stan_konta += self.przelicz_banknoty_klienta(nominaly_klienta=None)

    def oblicz_reszte(self, zamowienie):
        return self.przelicz_banknoty_klienta(nominaly_klienta=None) - zamowienie.oblicz_wysokosc_zamowienia()






