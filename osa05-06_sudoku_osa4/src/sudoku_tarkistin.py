# tee ratkaisu tänne
def sudoku_oikein(sudoku: list):
    # Tarkistetaan koko ruudukon rivit
    for rivi in range(9):
        sallittu_rivi = rivi_oikein(sudoku, rivi)
        if not sallittu_rivi:
            return False

    # Tarkistetaan koko ruudukon sarakkeet
    for sarake in range(9):
        sallittu_sarake = sarake_oikein(sudoku, sarake)
        if not sallittu_sarake:
            return False

    # Tarkistetaan kaikki yhdeksän 3x3 ruudukkoa
    for rivi in range(0, 7, 3):
        for sarake in range(0, 7, 3):
            sallittu_nelio = nelio_oikein(sudoku, rivi, sarake)
            if not sallittu_nelio:
                return False

    return True


def rivi_oikein(sudoku: list, rivi_nro: int):
    luetut_luvut = []
    rivi = sudoku[rivi_nro]
    for luku in rivi:
        if luku > 0 and luku in luetut_luvut:
            return False
        luetut_luvut.append(luku)

    return True


def sarake_oikein(sudoku: list, sarake_nro: int):
    luetut_luvut = []
    for rivi in sudoku:
        luku = rivi[sarake_nro]
        if luku > 0 and luku in luetut_luvut:
            return False
        luetut_luvut.append(luku)

    return True


def nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int):
    luvut = []
    for rivi in range(rivi_nro, rivi_nro+3):
        for ruutu in range(sarake_nro, sarake_nro + 3):
            luku = sudoku[rivi][ruutu]
            if luku > 0 and luku in luvut:
                return False
            luvut.append(luku)

    return True


if __name__ == '__main__':
    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_oikein(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_oikein(sudoku2))
