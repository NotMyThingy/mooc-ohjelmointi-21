# tee ratkaisu tänne
def lue(komento: str, ala: int, yla: int):
    while True:
        try:
            luku = int(input('syötä luku: '))
            if ala <= luku <= yla:
                return luku
        except:
            pass

        print(f'Syötteen on oltava kokonaisluku väliltä {ala}...{yla}')


if __name__ == '__main__':
    luku = lue("syötä luku: ", 5, 10)
    print("syötit luvun:", luku)
