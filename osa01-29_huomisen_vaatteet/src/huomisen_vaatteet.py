# Kirjoita ratkaisu tähän
print("Kerro huominen sääennuste: ")
lampotila = int(input("Lämpötila: "))
sataako = input("Sataako (kyllä/ei): ")

print("Pue housut ja t-paita")
if lampotila <= 20:
    print("Ota myös pitkähihainen paita")

if lampotila <= 10:
    print("Pue päälle takki")

if lampotila <= 5:
    print("Suosittelen lämmintä takkia")
    print("Kannattaa ottaa myös hanskat")

if sataako == "kyllä":
    print("Muista sateenvarjo!")
