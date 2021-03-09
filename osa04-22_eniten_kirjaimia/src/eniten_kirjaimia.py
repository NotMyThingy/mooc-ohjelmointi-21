# tee ratkaisu tänne
def eniten_kirjainta(mjono: str):
    eniten = mjono[0]
    for merkki in mjono:
        if mjono.count(merkki) > mjono.count(eniten):
            eniten = merkki
    return eniten


if __name__ == '__main__':
    mjono = "abcbdbe"
    print(eniten_kirjainta(mjono))

    toinen_jono = "esimerkkimerkkijonokki"
    print(eniten_kirjainta(toinen_jono))
