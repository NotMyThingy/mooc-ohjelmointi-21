class Pankkitili:

    def __init__(self, omistaja: str, tilinumero: str, saldo: float) -> None:
        self.__omistaja = omistaja
        self.__tilinumermo = tilinumero
        self.__saldo = saldo

    def talleta(self, summa: float):
        if summa > 0:
            self.__saldo += summa
            self.__palvelumaksu()
        else:
            raise ValueError('Negatiivin summa ei kelpaa')

    def nosta(self, summa: float):
        if summa <= self.__saldo:
            self.__saldo -= summa
            self.__palvelumaksu()
        else:
            raise ValueError('tilillä ei riittävästi varoja')

    @property
    def saldo(self):
        return self.__saldo

    def __palvelumaksu(self):
        self.__saldo = self.__saldo * 0.99


if __name__ == "__main__":
    tili = Pankkitili("Raimo Rahakas", "12345-6789", 1000)
    tili.nosta(100)
    print(tili.saldo)
    tili.talleta(100)
    print(tili.saldo)
