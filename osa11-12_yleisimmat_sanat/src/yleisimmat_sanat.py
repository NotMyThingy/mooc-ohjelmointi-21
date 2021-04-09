# TEE RATKAISUSI TÄHÄN:
from string import punctuation


def yleisimmat_sanat(tiedoston_nimi: str, raja: int):
    with open(tiedoston_nimi) as tiedosto:
        sisalto = tiedosto.read()
        sisalto = sisalto.replace('\n', '')
        for merkki in punctuation:
            sisalto = sisalto.replace(merkki, '')

        sanat = sisalto.split()
        return {sana: sanat.count(sana) for sana in sanat if sanat.count(sana) >= raja}


if __name__ == "__main__":
    print(yleisimmat_sanat("comprehensions.txt", 3))
