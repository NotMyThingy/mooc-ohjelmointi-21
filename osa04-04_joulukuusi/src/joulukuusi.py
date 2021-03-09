# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def tulostaTahtia(maara):
    print('*' * maara)


def tulostaTyhjaa(maara):
    print(' ' * maara, end='')


def joulukuusi(koko):
    print('joulukuusi!')

    korkeus = 1
    while korkeus <= koko:
        tulostaTyhjaa(koko - korkeus)
        tulostaTahtia(2 * korkeus - 1)
        korkeus += 1

    tulostaTyhjaa(koko - 1)
    tulostaTahtia(1)


if __name__ == "__main__":
    joulukuusi(5)
