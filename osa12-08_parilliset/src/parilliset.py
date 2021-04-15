def parilliset(alku: int, maksimi: int):
    luku = alku if alku % 2 == 0 else alku + 1
    while luku <= maksimi:
        yield luku
        luku += 2


if __name__ == "__main__":
    luvut = parilliset(11, 21)
    for luku in luvut:
        print(luku)
