# tee ratkaisu tänne
def luvuista_suurin(eka, toka, kolmas):
    if toka <= eka >= kolmas:
        return eka
    elif eka <= toka >= kolmas:
        return toka
    else:
        return kolmas


if __name__ == "__main__":
    suurin = luvuista_suurin(1, 1, -100)
    print(suurin)
