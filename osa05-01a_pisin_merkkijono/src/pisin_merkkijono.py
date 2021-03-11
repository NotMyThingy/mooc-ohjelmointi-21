# tee ratkaisu tänne
def pisin(merkkijonot: list):
    pisin = ''
    for mjono in merkkijonot:
        if len(mjono) > len(pisin):
            pisin = mjono
    return pisin


if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))
