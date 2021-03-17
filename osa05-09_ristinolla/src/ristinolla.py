# tee ratkaisu tänne
def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):
    if x < 0 or x > 2 or y < 0 or y > 2:
        return False

    if lauta[y][x] != '':
        return False

    lauta[y][x] = nappula
    return True


def main():
    lauta = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(pelaa_siirto(lauta, 2, 0, "X"))
    print(lauta)


if __name__ == '__main__':
    main()
