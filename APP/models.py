from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.fields.related import ForeignKey

class Nap(models.Model):

    sorszam = models.IntegerField()
    hosszu = models.CharField(max_length=20)
    rovid = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Nap'
        verbose_name_plural = 'Napok'

    def __str__(self):
        return self.hosszu

class Tantargy(models.Model):

    sorszam = models.IntegerField()
    kreta = models.CharField(max_length=50)
    hosszu = models.CharField(max_length=20)
    rovid = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Tantárgy'
        verbose_name_plural = 'Tantárgyak'

    def __str__(self):
        return self.kreta


class Szarny(models.Model):

    sorszam = models.IntegerField()
    hosszu = models.CharField(max_length=20)
    rovid = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Szárny'
        verbose_name_plural = 'Szárnyak'

    def __str__(self):
        return self.hosszu


class Terem(models.Model):

    sorszam = models.IntegerField()
    kreta = models.CharField(max_length=50)
    hosszu = models.CharField(max_length=50)
    rovid = models.CharField(max_length=20)
    emelet = models.IntegerField()
    szarny = models.ForeignKey(Szarny, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Terem'
        verbose_name_plural = 'Termek'

    def __str__(self):
        return self.kreta
        

class Osztaly(models.Model):

    sorszam = models.IntegerField()
    kreta = models.CharField(max_length=50)
    evfolyam = models.CharField(max_length=5)
    kor = models.CharField(max_length=5)
    szekcio = models.CharField(max_length=1)

    class Meta:
        verbose_name = 'Osztály'
        verbose_name_plural = 'Osztályok'

    def __str__(self):
        return self.kreta

    def tomorites(osztalylista) -> str:
        sum = ''
        for evf in ['ny','9','10','11','12']:
            evfolyamlista = [x for x in osztalylista if evf == x.evfolyam]
            if len(evfolyamlista)>0:
                sum+=evf
                for osztaly in evfolyamlista:
                    sum+=osztaly.szekcio.lower()
        return sum

        

class Tanar(models.Model):

    sorszam = models.IntegerField()
    kreta = models.CharField(max_length=50)
    hosszu = models.CharField(max_length=50)
    rovid = models.CharField(max_length=20)
    monogram = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Tanár'
        verbose_name_plural = 'Tanárok'

    def __str__(self):
        return self.kreta


class Munkakozosseg(models.Model):

    sorszam = models.IntegerField()
    nev = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Munkaközösség'
        verbose_name_plural = 'Munkaközösségek'

    def __str__(self):
        return self.nev

class MTK(models.Model):

    tanar = models.ForeignKey(Tanar, on_delete=models.CASCADE)
    munkakozosseg = models.ForeignKey(Munkakozosseg, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Munkaközösség-Tanar kapcsolat'
        verbose_name_plural = 'Munkaközösség-Tanar kapcsolatok'

    def __str__(mtk):
        return mtk.tanar.rovid + " -> " + mtk.munkakozosseg.nev
        

class Csoport(models.Model):

    kreta = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Csoport'
        verbose_name_plural = 'Csoportok'

    def __str__(self):
        return self.kreta

    @property
    def osztalyai(a_csoport):
        return Osztaly.tomorites([ x.osztaly for x in CSOK.objects.filter(csoport=a_csoport)])





# CSOK = Csoport-Osztály-Kapcsolat
class CSOK(models.Model):

    csoport = models.ForeignKey(Csoport, on_delete=models.CASCADE)
    osztaly = models.ForeignKey(Osztaly, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Csoport-Osztály kapcsolat'
        verbose_name_plural = 'Csoport-Osztály kapcsolatok'

    def __str__(csok):
        return str(csok.csoport) + " -> " + str(csok.osztaly)


class Ora(models.Model):

    nap = models.ForeignKey(Nap, on_delete=models.CASCADE)
    ora = models.IntegerField()
    csoport = models.ForeignKey(Csoport, on_delete=models.CASCADE)
    tantargy = models.ForeignKey(Tantargy, on_delete=models.CASCADE)
    tanar = models.ForeignKey(Tanar, on_delete=models.CASCADE)
    terem = models.ForeignKey(Terem, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Óra'
        verbose_name_plural = 'Óra'

    def __str__(o):
        return f'{o.nap.hosszu} {o.ora}.: {o.tanar} --- {o.tantargy.rovid} --> {o.csoport} [{o.terem}]  '


