# tee ratkaisu tänne
def sanat_pisteella(hakusana: str, sanat: list):
    loydetyt = []
    for sana in sanat:
        if len(sana) != len(hakusana):
            continue

        osuma = True
        for i in range(len(hakusana)):
            if hakusana[i] == ".":
                pass
            elif hakusana[i] != sana[i]:
                osuma = False
                break

        if osuma:
            loydetyt.append(sana)

    return loydetyt


def sanat_tahdella(hakusana: str, sanat: str):
    loydetyt = []
    hakusana_ilman_tahtea = hakusana.replace('*', '')
    for sana in sanat:
        if hakusana.endswith("*"):
            if sana.startswith(hakusana_ilman_tahtea):
                loydetyt.append(sana)
        elif hakusana.startswith("*"):
            if sana.endswith(hakusana_ilman_tahtea):
                loydetyt.append(sana)

    return loydetyt


def hae_samat(hakusana, sanat):
    loydetyt = []
    for sana in sanat:
        if sana == hakusana:
            loydetyt.append(sana)

    return loydetyt


def hae_sanat(hakusana: str):
    sanat = []
    with open('sanat.txt') as tiedosto:
        for sana in tiedosto:
            sanat.append(sana.strip())

    if "." in hakusana:
        loydetyt = sanat_pisteella(hakusana, sanat)
    elif "*" in hakusana:
        loydetyt = sanat_tahdella(hakusana, sanat)
    else:
        loydetyt = hae_samat(hakusana, sanat)

    return loydetyt


if __name__ == '__main__':
    print(hae_sanat("vag*"))
