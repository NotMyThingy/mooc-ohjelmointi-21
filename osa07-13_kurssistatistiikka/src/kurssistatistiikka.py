# tee ratkaisu tänne
import urllib.request
import json
from math import ceil, floor


def hae_kaikki():
    req = urllib.request.urlopen('https://studies.cs.helsinki.fi/stats-mock/api/courses')
    kurssi_data = json.loads(req.read())
    kurssit = []
    for kurssi in kurssi_data:
        if kurssi['enabled']:
            fullname = kurssi['fullName']
            name = kurssi['name']
            year = kurssi['year']
            exercises = sum(kurssi['exercises'])
            k = fullname, name, year, exercises
            kurssit.append(k)

    return kurssit


def hae_kurssi(kurssi: str):
    req = urllib.request.urlopen(f'https://studies.cs.helsinki.fi/stats-mock/api/courses/{kurssi}/stats')
    kurssi_viikot = json.loads(req.read())
    opiskelijoita = 0
    tunteja = 0
    tehtavia = 0
    for nro, viikko in kurssi_viikot.items():
        if viikko['students'] > opiskelijoita:
            opiskelijoita = viikko['students']
        tunteja += viikko['hour_total']
        tehtavia += viikko['exercise_total']

    return {
        'viikkoja': len(kurssi_viikot),
        'opiskelijoita': opiskelijoita,
        'tunteja': tunteja,
        'tunteja_keskimaarin': tunteja // opiskelijoita,
        'tehtavia': tehtavia,
        'tehtavia_keskimaarin': tehtavia // opiskelijoita
    }


if __name__ == '__main__':
    print(hae_kurssi("docker2019"))
