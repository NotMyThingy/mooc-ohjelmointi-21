# tee ratkaisu tänne
def uusi_henkilo(nimi: str, ika: int):
    if nimi == '' or nimi.count(' ') == 0 or len(nimi) > 40:
        raise ValueError(f'nimi [{nimi}] ei kelpaa')
    elif ika < 0 or ika > 150:
        raise ValueError(f'ikä [{ika}] ei kelpaa')

    return nimi, ika


if __name__ == '__main__':
    h = uusi_henkilo('massa masa', 154)
    print(h)
