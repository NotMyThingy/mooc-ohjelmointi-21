# TEE RATKAISUSI TÄHÄN:
class Auto:

    def __init__(self) -> None:
        self.__bensaa = 0
        self.__ajettu = 0

    def tankkaa(self):
        self.__bensaa = 60

    def aja(self, km: int):
        if km > self.__bensaa:
            km = self.__bensaa

        self.__ajettu += km
        self.__bensaa -= km

    def __str__(self) -> str:
        return f'Auto: ajettu {self.__ajettu} km, bensaa {self.__bensaa} litraa'


auto = Auto()
print(auto)
auto.tankkaa()
print(auto)
auto.aja(20)
print(auto)
auto.aja(50)
print(auto)
auto.aja(10)
print(auto)
auto.tankkaa()
auto.tankkaa()
print(auto)
