# tee ratkaisu tänne
def tulosta(sudoku: list):
    for rivi in range(len(sudoku)):
        # lisätään tyhjä rivi, jos kolme alekkain
        if rivi % 3 == 0:
            print()

        for sarake in range(len(sudoku)):
            # lisätään välilyönti, jos kolme rivissä
            if sarake > 0 and sarake % 3 == 0:
                print(' ', end='')

            if sudoku[rivi][sarake] == 0:
                print('_ ', end='')
            else:
                print(f'{sudoku[rivi][sarake]} ', end='')

        print()


def kopioi_ja_lisaa(sudoku: list, rivi_nro: int, sarake_nro: int, luku: int):
    kopio = []
    for rivi in sudoku:
        kopio.append(rivi[:])

    kopio[rivi_nro][sarake_nro] = luku
    return kopio


def main():
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    kopio = kopioi_ja_lisaa(sudoku, 4, 2, 2)
    print("Alkuperäinen:")
    tulosta(sudoku)
    print()
    print("Kopio:")
    tulosta(kopio)


if __name__ == "__main__":
    main()
