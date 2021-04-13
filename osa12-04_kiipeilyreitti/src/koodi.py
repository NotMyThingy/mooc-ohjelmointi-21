class Kiipeilyreitti:
    def __init__(self, nimi: str, pituus: int, grade: str):
        self.nimi = nimi
        self.pituus = pituus
        self.grade = grade

    def __str__(self):
        return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}"


def pituuden_mukaan(reitit: list):
    def pituus(reitti: Kiipeilyreitti):
        return reitti.pituus
    return sorted(reitit, key=pituus, reverse=True)


# järjestetään vaikeuden mukaan. jos kaksi samaa, niin nimen mukaan
def vaikeuden_mukaan(reitit: list):
    def vaikeus_tai_pituus(reitti: Kiipeilyreitti):
        return reitti.grade, reitti.pituus
    return sorted(reitit, key=vaikeus_tai_pituus, reverse=True)


if __name__ == '__main__':
    r1 = Kiipeilyreitti("Kantti", 38, "6A+")
    r2 = Kiipeilyreitti("Smooth operator", 11, "7A")
    r3 = Kiipeilyreitti("Syncro", 14, "8C+")
    r4 = Kiipeilyreitti("Pieniä askelia", 12, "6A+")

    reitit = [r1, r2, r3, r4]
    for reitti in vaikeuden_mukaan(reitit):
        print(reitti)
