# tee ratkaisu tänne
def tallenna_henkilo(henkilo: tuple):
    with open('henkilot.csv', 'a') as tiedosto:
        tiedosto.write(f'{henkilo[0]};{henkilo[1]};{henkilo[2]}')


if __name__ == '__main__':
    tallenna_henkilo(("Kimmo Kimmonen", 37, 175.5))
