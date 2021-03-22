import math


def hae_asematiedot(tiedosto: str):
    asemat = {}
    with open(tiedosto) as asematiedot:
        for rivi in asematiedot:
            tiedot = rivi.split(';')
            if tiedot[0] == 'Longitude':
                continue
            asemat[tiedot[3]] = (float(tiedot[0]), float(tiedot[1]))

    return asemat


def etaisyys(tiedosto: dict, as1: str, as2: str):
    asema1 = tiedosto[as1]
    asema2 = tiedosto[as2]

    x_in_km = (asema1[0] - asema2[0]) * 55.26
    y_in_km = (asema1[1] - asema2[1]) * 111.2
    dist = math.sqrt(x_in_km**2 + y_in_km**2)

    return dist


def suurin_etaisyys(asemat: dict):
    pisin = ('', '', 0)
    for asema1 in asemat:
        for asema2 in asemat:
            et = etaisyys(asemat, asema1, asema2)
            if et > pisin[2]:
                pisin = asema1, asema2, et

    return pisin


def main():
    asemat = hae_asematiedot('stations1.csv')
    asema1, asema2, suurin = suurin_etaisyys(asemat)
    print(asema1, asema2, suurin)


if __name__ == '__main__':
    main()
