# Kirjoita ratkaisu tähän
luvut = []
lukuja = int(input('Kuinka monta lukua: '))
while(lukuja > 0):
    luku = int(input('Anna luku: '))
    luvut.append(luku)
    lukuja -= 1

print(luvut)
