# tee ratkaisu tänne
def histogrammi(mjono: str):
    kirjaimet = {}
    for kirjain in mjono:
        if kirjain not in kirjaimet:
            kirjaimet[kirjain] = 0
        kirjaimet[kirjain] += 1

    for kirjain in kirjaimet:
        print(f'{kirjain} {kirjaimet[kirjain] * "*"}')


if __name__ == "__main__":
    histogrammi('abba')
