# tee ratkaisu tänne
def transponoi(matriisi: list):
    kopio = []
    for rivi in matriisi:
        kopio.append(rivi[:])

    for x in range(len(matriisi)):
        for y in range(len(matriisi)):
            matriisi[y][x] = kopio[x][y]
