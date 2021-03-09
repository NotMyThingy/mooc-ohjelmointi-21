# tee ratkaisu tänne
def viiva(leveys, mjono):
    if len(mjono) == 0:
        mjono = '*'

    print(mjono[0] * leveys)


if __name__ == "__main__":
    viiva(5, "")
