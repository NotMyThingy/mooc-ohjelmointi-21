# tee ratkaisu tänne
def lyhin(nimet: list):
    lyhin = ""

    for nimi in nimet:
        if lyhin == "" or len(nimi) < len(lyhin):
            lyhin = nimi

    return lyhin


if __name__ == "__main__":
    nimet = ['Arto', 'Leena', 'Santeri', 'Kim', 'Minna']

    tulos = lyhin(nimet)
    print(tulos)
