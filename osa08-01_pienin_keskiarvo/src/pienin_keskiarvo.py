# tee ratkaisu tänne
def keskiarvo(henkilo: dict):
    return sum([henkilo['tulos1'], henkilo['tulos2'], henkilo['tulos3']]) / 3


def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):
    h1 = keskiarvo(henkilo1)
    h2 = keskiarvo(henkilo2)
    h3 = keskiarvo(henkilo3)

    if h2 > h1 < h3:
        return henkilo1
    if h1 > h2 < h3:
        return henkilo2
    return henkilo3


if __name__ == '__main__':
    henkilo1 = {"nimi": "Keijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
    henkilo2 = {"nimi": "Reijo", "tulos1": 5, "tulos2": 1, "tulos3": 8}
    henkilo3 = {"nimi": "Veijo", "tulos1": 3, "tulos2": 1, "tulos3": 1}

    print(pienin_keskiarvo(henkilo1, henkilo2, henkilo3))
