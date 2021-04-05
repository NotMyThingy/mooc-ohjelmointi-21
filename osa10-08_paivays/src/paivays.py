# Tässä tehtävässä toteutetaan luokka Paivays, jonka avulla on mahdollista käsitellä päivämääriä.
# Oletetaan tässä tehtävässä yksinkertaisuuden vuoksi, että jokaisessa kuussa on 30 päivää.

class Paivays:
    def __init__(self, paiva: int, kuukausia: int, vuosi: int):
        self.__paiva = paiva
        self.__kuukausi = kuukausia
        self.__vuosi = vuosi

    def __str__(self):
        return f'{self.__paiva}.{self.__kuukausi}.{self.__vuosi}'

    # apumetodi palauttaa päivämäärän muutettuna päiviksi
    def paiviksi(self):
        return self.__paiva + self.__kuukausi * 30 + self.__vuosi * 360

    # apumetodi palauttaa uuden Paivays-olion
    def uusi_paivays(self, paivia: int):
        kuukausia = paivia // 30
        vuosia = kuukausia // 12
        paivia -= kuukausia * 30
        kuukausia -= vuosia * 12
        return Paivays(paivia, kuukausia, vuosia)

    def __lt__(self, toinen):
        return self.paiviksi() < toinen.paiviksi()

    def __gt__(self, toinen):
        return self.paiviksi() > toinen.paiviksi()

    def __eq__(self, toinen):
        return self.paiviksi() == toinen.paiviksi()

    def __ne__(self, toinen):
        return self.paiviksi() != toinen.paiviksi()

    def __add__(self, paivia: int):
        return self.uusi_paivays(self.paiviksi() + paivia)

    def __sub__(self, toinen):
        return abs(self.paiviksi() - toinen.paiviksi())


if __name__ == "__main__":
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(2, 11, 2020)
    p3 = Paivays(28, 12, 1985)

    print(p2-p1)
    print(p1-p2)
    print(p1-p3)
