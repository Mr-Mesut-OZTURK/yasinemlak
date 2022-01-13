from django.contrib import admin
from .models import (
    EmlakTipi,
    OdaSayisi,
    IsitmaDurumu,
    EmlakKayit,
    EmlakKayitFoto,

    MainSlider,
    Message
)

# Register your models here.
class EmlakKayitInline(admin.TabularInline):
    model = EmlakKayitFoto

class EmlakKayitAdmin(admin.ModelAdmin):
    inlines = [EmlakKayitInline]

    class Meta:
        model = EmlakKayit



admin.site.register(EmlakTipi)
admin.site.register(OdaSayisi)
admin.site.register(IsitmaDurumu)
admin.site.register(EmlakKayit, EmlakKayitAdmin)
admin.site.register(EmlakKayitFoto)

admin.site.register(MainSlider)

admin.site.register(Message)