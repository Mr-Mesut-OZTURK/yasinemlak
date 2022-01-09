from django.db import models

# Create your models here.


class EmlakTipi(models.Model):
    isim = models.CharField(max_length=250)

    def __str__(self):
        return self.isim


class OdaSayisi(models.Model):
    isim = models.CharField(max_length=10)

    def __str__(self):
        return self.isim

class IsitmaDurumu(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
        return self.isim

class EvKayit(models.Model):
    baslik = models.CharField(max_length=250)

    olusturulma_tarihi = models.DateField(auto_now=True)
    yayinlama_tarihi = models.DateField(auto_now_add=True)
    yayimla = models.BooleanField(default=False)

    DURUMU = (
        (1, "kiralık"),
        (2, "satılık")
    )

    durumu = models.CharField(max_length=250, choices=DURUMU)

    fiyat = models.PositiveIntegerField()
    metrekare = models.PositiveIntegerField()

    emlak_tipi = models.ForeignKey(EmlakTipi, ondelete=models.PROTECT)
    oda_sayısı = models.ForeignKey(OdaSayisi, ondelete=models.PROTECT)
    isitma_durumu = models.ForeignKey(IsitmaDurumu, ondelete=models.PROTECT)

    def __str__(self):
        return f"{self.id} - {self.baslik}"

class EvKayitFoto(models.Model):
    foto = models.ImageField(upload_to="evler/%Y/%m")
    ev_kayit = models.ForeignKey(EvKayit, ondelete=models.CASCADE)



#######################################################################

class ArsaTipi(models.Model):
    isim = models.CharField(max_length=10)

    def __str__(self):
        return self.isim

class ArsaKayit(models.Model):
    baslik = models.CharField(max_length=250)

    olusturulma_tarihi = models.DateField(auto_now=True)
    yayinlama_tarihi = models.DateField(auto_now_add=True)
    yayimla = models.BooleanField(default=False)

    DURUMU = (
        (1, "kiralık"),
        (2, "satılık")
    )

    durumu = models.CharField(max_length=250, choices=DURUMU)

    fiyat = models.PositiveIntegerField()
    metrekare = models.PositiveIntegerField()

    arsa_tipi = models.ForeignKey(ArsaTipi, ondelete=models.PROTECT)
    # oda_sayısı = models.ForeignKey(OdaSayisi, ondelete=models.PROTECT)
    # isitma_durumu = models.ForeignKey(IsitmaDurumu, ondelete=models.PROTECT)

    def __str__(self):
        return f"{self.id} - {self.baslik}"

class ArsaKayitFoto(models.Model):
    foto = models.ImageField(upload_to="evler/%Y/%m")
    arsa_kayit = models.ForeignKey(EvKayit, ondelete=models.CASCADE)
