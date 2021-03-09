# tee ratkaisu tänne
def ilman_vokaaleja(mjono):
    vokaalit = ('a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö')
    for merkki in mjono:
        if merkki in vokaalit:
            mjono = mjono.replace(merkki, '')
    return mjono


if __name__ == '__main__':
    mjono = "tämä on esimerkki"
    print(ilman_vokaaleja(mjono))
