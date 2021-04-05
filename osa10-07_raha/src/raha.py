# TEE RATKAISUSI TÄHÄN:
class Raha:
    def __init__(self, eurot: int, sentit: int):
        self.__eurot = eurot
        self.__sentit = sentit

    def __str__(self):
        return f"{self.__eurot}.{self.__sentit:0>2} eur"

    # apumetodi palauttaa silloisen rahamäärän sentteinä
    def __sentteina(self):
        return self.__eurot * 100 + self.__sentit

    # apumetodi muuntaa sentit euroiksi ja palauttaa uuden raha-olion
    def __rahaksi(self, sentteina):
        eurot = sentteina // 100
        sentit = sentteina % 100
        return Raha(eurot, sentit)

    def __eq__(self, toinen):
        return self.__sentteina() == toinen.__sentteina()

    def __gt__(self, toinen):
        return self.__sentteina() > toinen.__sentteina()

    def __lt__(self, toinen):
        return self.__sentteina() < toinen.__sentteina()

    def __ne__(self, toinen):
        return self.__sentteina() != toinen.__sentteina()

    def __add__(self, toinen):
        sentteina = self.__sentteina() + toinen.__sentteina()
        return self.__rahaksi(sentteina)

    def __sub__(self, toinen):
        sentteina = self.__sentteina() - toinen.__sentteina()
        if sentteina < 0:
            raise ValueError('arvo ei voi olla negatiivinen')
        return self.__rahaksi(sentteina)


if __name__ == "__main__":
    e1 = Raha(4, 5)
    print(e1)
    e1.eurot = 1000
    print(e1)
