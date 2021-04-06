# Tee ratkaisusi tähän:
class Tavara:

    def __init__(self, nimi: str, paino: int) -> None:
        self.__nimi = nimi
        self.__paino = paino

    def nimi(self) -> str:
        return self.__nimi

    def paino(self) -> int:
        return self.__paino

    def __str__(self) -> str:
        return f'{self.__nimi} ({self.__paino} kg)'


class Matkalaukku:

    def __init__(self, maksimipaino: int) -> None:
        self.__maksimipaino = maksimipaino
        self.__tavarat = {}

    def lisaa_tavara(self, tavara: Tavara):
        if tavara.paino() + self.paino() <= self.__maksimipaino:
            self.__tavarat[tavara] = tavara.paino()

    def tulosta_tavarat(self):
        for tavara in self.__tavarat.keys():
            print(tavara)

    def paino(self):
        return sum(self.__tavarat.values())

    def raskain_tavara(self):
        raskain = None
        for tavara in self.__tavarat.keys():
            if raskain == None or tavara.paino() > raskain.paino():
                raskain = tavara
        return raskain

    def __str__(self) -> str:
        a = '' if len(self.__tavarat) == 1 else 'a'
        return f'{len(self.__tavarat)} tavara{a} ({self.paino()} kg)'


class Lastiruuma:

    def __init__(self, maksimipaino: int) -> None:
        self.__maksimipaino = maksimipaino
        self.__matkalaukut = {}

    def lisaa_matkalaukku(self, matkalaukku: Matkalaukku):
        if matkalaukku.paino() + self.paino() <= self.__maksimipaino:
            self.__matkalaukut[matkalaukku] = matkalaukku.paino()

    def paino(self):
        return sum(self.__matkalaukut.values())

    def tulosta_tavarat(self):
        for matkalaukku in self.__matkalaukut:
            matkalaukku.tulosta_tavarat()

    def __str__(self) -> str:
        a = '' if len(self.__matkalaukut) == 1 else 'a'
        return f'{len(self.__matkalaukut)} matkalaukku{a}, tilaa {self.__maksimipaino - self.paino()} kg'


if __name__ == '__main__':
    kirja = Tavara("Aapiskukko", 2)
    puhelin = Tavara("Nokia 3210", 1)
    tiiliskivi = Tavara("Tiiliskivi", 4)

    adan_laukku = Matkalaukku(10)
    adan_laukku.lisaa_tavara(kirja)
    adan_laukku.lisaa_tavara(puhelin)

    pekan_laukku = Matkalaukku(10)
    pekan_laukku.lisaa_tavara(tiiliskivi)

    lastiruuma = Lastiruuma(1000)
    lastiruuma.lisaa_matkalaukku(adan_laukku)
    lastiruuma.lisaa_matkalaukku(pekan_laukku)

    print("Ruuman matkalaukuissa on seuraavat tavarat:")
    lastiruuma.tulosta_tavarat()
