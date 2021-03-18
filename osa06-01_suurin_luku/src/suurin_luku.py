# tee ratkaisu tänne
def suurin():
    with open('luvut.txt') as tiedosto:
        suurin = -9999
        for luku in tiedosto:
            luku = int(luku.replace('\n', ''))
            if luku > suurin:
                suurin = luku

    return suurin


if __name__ == '__main__':
    print(suurin())
