# tee ratkaisu tänne
def kertaa_kymmenen(alku: int, loppu: int):
    luvut = {}
    for luku in range(alku, loppu+1):
        luvut[luku] = luku * 10

    return luvut


d = kertaa_kymmenen(3, 6)
print(d)
