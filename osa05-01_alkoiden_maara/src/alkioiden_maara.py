# tee ratkaisu tänne
def laske_alkiot(matriisi: list, etsitty_alkio: int):
    monesti_taulukossa = 0
    for rivi in matriisi:
        for alkio in rivi:
            if alkio == etsitty_alkio:
                monesti_taulukossa += 1
    return monesti_taulukossa


if __name__ == '__main__':
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(laske_alkiot(m, 1))
