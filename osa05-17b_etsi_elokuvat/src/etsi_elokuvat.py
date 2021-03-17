# tee ratkaisu tänne
def etsi_elokuvat(rekisteri: list, hakusana: str):
    haku_tulokset = []
    for elokuva in rekisteri:
        if hakusana.lower() in elokuva['nimi'].lower():
            haku_tulokset.append(elokuva)

    return haku_tulokset


def main():
    rekisteri = [{"nimi": "Pythonin viemää", "ohjaaja": "Pekka Python", "vuosi": 2017, "pituus": 116},
                 {"nimi": "Python lentokoneessa", "ohjaaja": "Renny Pythonen",
                     "vuosi": 2001, "pituus": 94},
                 {"nimi": "Koodaajien yö", "ohjaaja": "M. Night Python", "vuosi": 2011, "pituus": 101}]

    lista = etsi_elokuvat(rekisteri, "python")
    print(lista)


if __name__ == '__main__':
    main()
