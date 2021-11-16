print('------ inic.py indul')

from APP.models import *
from django.contrib.auth.models import User, Group


def csv2dictlistreversible(fajlnev):
    mezonevek_sora=''
    with open(fajlnev, 'r', encoding="utf-8") as f:
        mezonevek_sora = f.readline()
        mezonevek = mezonevek_sora.strip().split(',')+['sor']
        return list(map(lambda sor : dict(zip(mezonevek, sor.strip().split(',')+[sor])), f))

def csv2dictlist(csvpath):
    mezonevek_sora=''
    with open(csvpath, 'r', encoding="utf-8") as f:
        mezonevek_sora = f.readline()  
        mezonevek = mezonevek_sora.strip().split(',')
        return list(map(lambda sor : dict(zip(mezonevek, sor.strip().split(','))), f))

def csv2table(osztaly, csvpath, kapcsolatok=[]): # csv feltétlen tartalmazza az (ékezetmentes stb.?) mezőneveket, amelyek megegyeznek a tábla mezőneveivel!
    for rekord in csv2dictlist(csvpath):
        for kapcsolat in kapcsolatok:
            kwargs = {kapcsolat['tabla_kulcs']:rekord[kapcsolat['idegen_kulcs']]}
            rekord[kapcsolat['idegen_kulcs']] = kapcsolat['tabla'].objects.get(**kwargs)
        osztaly.objects.get_or_create(**rekord)
    print(f"--- inic.py: {csvpath} fájl adattáblává alakítva")


"""  létfontosságú csoportok feldolgozása  """

Group.objects.get_or_create(name='adminisztrator')[0]  
Group.objects.get_or_create(name='latogato')[0] 

print("--- inic.py: létfontosságú csoportok létrejöttek")

""" csv fájlok feldolgozása """

csv2table(Nap, "csvs/nap.csv")
csv2table(Tantargy, "csvs/tantargy.csv")
csv2table(Szarny, "csvs/szarny.csv")
csv2table(Terem, "csvs/terem.csv", [
    {
        'tabla': Szarny, 
        'idegen_kulcs': 'szarny',
        'tabla_kulcs': 'hosszu'
    },
])
csv2table(Tanar, "csvs/tanar.csv")
csv2table(Munkakozosseg, "csvs/munkakozosseg.csv")
csv2table(MTK, "csvs/mtk.csv", [
    {
        'tabla': Tanar, 
        'idegen_kulcs': 'tanar',
        'tabla_kulcs': 'kreta'
    },
    {
        'tabla': Munkakozosseg, 
        'idegen_kulcs': 'munkakozosseg',
        'tabla_kulcs': 'nev'
    },
])
csv2table(Osztaly, "csvs/osztaly.csv")
csv2table(Csoport, "csvs/csoport.csv")
csv2table(CSOK, "csvs/csok.csv", [
    {
        'tabla': Csoport, 
        'idegen_kulcs': 'csoport',
        'tabla_kulcs': 'kreta'
    },
    {
        'tabla': Osztaly, 
        'idegen_kulcs': 'osztaly',
        'tabla_kulcs': 'kreta'
    },
])
csv2table(Ora, "csvs/ora.csv", [
    {
        'tabla': Nap, 
        'idegen_kulcs': 'nap',
        'tabla_kulcs': 'sorszam'
    },
    {
        'tabla': Csoport, 
        'idegen_kulcs': 'csoport',
        'tabla_kulcs': 'kreta'
    },
    {
        'tabla': Tantargy, 
        'idegen_kulcs': 'tantargy',
        'tabla_kulcs': 'kreta'
    },
    {
        'tabla': Tanar, 
        'idegen_kulcs': 'tanar',
        'tabla_kulcs': 'kreta'
    },
    {
        'tabla': Terem, 
        'idegen_kulcs': 'terem',
        'tabla_kulcs': 'kreta'
    },
])






print("--- inic.py: csv-fájlok alapján elkészült az adatbázis")

print("------ inic.py befejeződött")




