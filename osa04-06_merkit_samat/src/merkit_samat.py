# tee ratkaisu tänne
def samat(mjono, i1, i2):
    if i1 not in range(len(mjono)) or i2 not in range(len(mjono)):
        return False

    return mjono[i1] == mjono[i2]


if __name__ == "__main__":
    print(samat("koodari", 1, 2))
