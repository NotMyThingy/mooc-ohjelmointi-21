# tee ratkaisu tänne
def kertomat(n: int):
    luvut = {}
    for luku in range(1, n+1):
        kertoma = 1
        for i in range(1, luku):
            kertoma *= i+1
        luvut[luku] = kertoma
    return luvut


if __name__ == '__main__':
    k = kertomat(5)
    print(k[1])
    print(k[3])
    print(k[5])
