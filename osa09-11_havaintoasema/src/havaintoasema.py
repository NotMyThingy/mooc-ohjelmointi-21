class Havaintoasema:

    def __init__(self, asema: str) -> None:
        self.__asema = asema
        self.__havainnot = []

    def lisaa_havainto(self, havainto: str):
        self.__havainnot.append(havainto)

    def viimeisin_havainto(self):
        if len(self.__havainnot) == 0:
            return ''
        return self.__havainnot[-1]

    def havaintojen_maara(self):
        return len(self.__havainnot)

    def __str__(self) -> str:
        return f'{self.__asema}, {self.havaintojen_maara()} havaintoa'


if __name__ == "__main__":
    asema = Havaintoasema("Kumpula")
    asema.lisaa_havainto("Sadetta 10mm")
    asema.lisaa_havainto("Aurinkoista")
    print(asema.viimeisin_havainto())
    
    asema.lisaa_havainto("Ukkosta")
    print(asema.viimeisin_havainto())
    
    print(asema.havaintojen_maara())
    print(asema)
