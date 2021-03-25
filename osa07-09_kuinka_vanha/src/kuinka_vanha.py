# tee ratkaisu tänne
from datetime import datetime

paiva = int(input('Päivä: '))
kuukausi = int(input('Kuukausi: '))
vuosi = int(input('Vuosi: '))

syntymapaiva = datetime(vuosi, kuukausi, paiva)
millenium = datetime(1999, 12, 31)

if millenium < syntymapaiva:
    print('Et ollut syntynyt, kun vuosituhat vaihtui.')
else:
    erotus = millenium - syntymapaiva
    print(f'Olit {erotus.days} päivää vanha, kun vuosituhat vaihtui.')
