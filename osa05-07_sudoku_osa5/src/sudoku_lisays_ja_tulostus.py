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


def lisays(sudoku: list, rivi_nro: int, sarake_nro: int, luku: int):
    sudoku[rivi_nro][sarake_nro] = luku


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

    tulosta(sudoku)
    lisays(sudoku, 0, 0, 2)
    lisays(sudoku, 1, 2, 7)
    lisays(sudoku, 5, 7, 3)
    print()
    print("Kolme numeroa lisätty:")
    print()
    tulosta(sudoku)


if __name__ == '__main__':
    main()
