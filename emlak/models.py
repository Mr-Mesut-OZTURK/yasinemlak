from django.db import models
from datetime import datetime

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

class EmlakKayit(models.Model):
    baslik = models.CharField(max_length=250)

    olusturulma_tarihi = models.DateField(auto_now=True)
    yayinlama_tarihi = models.DateField(auto_now_add=True)
    yayimla = models.BooleanField(default=False)

    DURUMU = (
        ("1", "kiralık"),
        ("2", "satılık")
    )

    durumu = models.CharField(max_length=250, choices=DURUMU)

    fiyat = models.PositiveIntegerField()
    metrekare = models.PositiveIntegerField()
    # bina_yası = models.PositiveIntegerField()
    resim = models.ImageField(upload_to="kapakresimler/evler/%Y/%m", null=True, blank=True)

    bina_yapım_yılı = models.DateField()
    bulundugu_kat = models.IntegerField()
    imar_durumu = models.CharField(max_length=250)

    emlak_tipi = models.ForeignKey(EmlakTipi, on_delete=models.SET_NULL, null=True)
    oda_sayısı = models.ForeignKey(OdaSayisi, on_delete=models.SET_NULL, null=True)
    isitma_durumu = models.ForeignKey(IsitmaDurumu, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.id} - {self.baslik}"



class EmlakKayitFoto(models.Model):
    foto = models.ImageField(upload_to="evler/%Y/%m")
    ev_kayit = models.ForeignKey(EmlakKayit, on_delete=models.CASCADE)


########################################################################

class MainSlider(models.Model):
    image = models.ImageField(upload_to="mainslider")
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return self.title