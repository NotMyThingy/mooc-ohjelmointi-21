# tee ratkaisu tänne
def kumpi_voitti(pelilauta: list):
    pelaaja1 = 0
    pelaaja2 = 0

    for rivi in pelilauta:
        for ruutu in rivi:
            if ruutu == 1:
                pelaaja1 += 1
            elif ruutu == 2:
                pelaaja2 += 1

    if pelaaja1 == pelaaja2:
        return 0
    else:
        return 1 if pelaaja1 > pelaaja2 else 2


if __name__ == '__main__':
    print(kumpi_voitti([[1, 1, 2], [1, 0, 2], [1, 2, 2]]))
