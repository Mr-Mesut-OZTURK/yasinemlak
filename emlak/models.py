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

    olusturulma_tarihi = models.DateField(auto_now_add=True)
    yayinlama_tarihi = models.DateField(auto_now=True)
    yayimla = models.BooleanField(default=False)

    # DURUMU = (
    #     ("1", "kiralık"),
    #     ("2", "satılık")
    # )
    # durumu = models.CharField(max_length=250, choices=DURUMU)

    fiyat = models.PositiveIntegerField()
    metrekare = models.PositiveIntegerField()
    resim = models.ImageField(upload_to="kapakresimler/evler/%Y/%m", null=True, blank=True)

    bina_yapım_yılı = models.DateField(null=True, blank=True)
    bulundugu_kat = models.IntegerField(null=True, blank=True)
    kat_sayisi = models.IntegerField(null=True, blank=True)
    imar_durumu = models.CharField(max_length=250, null=True, blank=True)

    emlak_acıklamat = models.TextField(null=True, blank=True)

    emlak_tipi = models.ForeignKey(EmlakTipi, on_delete=models.SET_NULL, null=True)
    oda_sayısı = models.ForeignKey(OdaSayisi, on_delete=models.SET_NULL, null=True, blank=True)
    isitma_durumu = models.ForeignKey(IsitmaDurumu, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.baslik}"



class EmlakKayitFoto(models.Model):
    foto = models.ImageField(upload_to="evler/%Y/%m/%d")
    ev_kayit = models.ForeignKey(EmlakKayit, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ev_kayit.baslik} - {self.id}"
########################################################################

class MainSlider(models.Model):
    image = models.ImageField(upload_to="mainslider")
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return self.title


################################################################

class Message(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=250)
    sender = models.EmailField()
    message = models.TextField()
    cc_myself = models.BooleanField(default=False)

    def __str__(self):
        return self.name