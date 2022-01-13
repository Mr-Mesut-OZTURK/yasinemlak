import datetime
from django.core.mail import send_mass_mail, send_mail

from django.shortcuts import get_object_or_404, render, redirect
from .models import (
    EmlakKayit,
    EmlakKayitFoto,
    MainSlider,

    EmlakTipi
    )
from . forms import ContactForm

# Create your views here.

def home(request):
    evler = EmlakKayit.objects.filter(yayimla=True)
    satilik = evler.filter(emlak_tipi__isim="satilik")
    kiralik = evler.filter(emlak_tipi__isim="kiralik")
    arsa = evler.filter(emlak_tipi__isim="arsa")
    slider = MainSlider.objects.all()
    # print(evler)
    content= {
        "satilik":satilik,
        "kiralik": kiralik,
        "arsa":arsa,
        "slider":slider
    }
    # print(content)
    return render(request, 'index.html', content)

def about(request):
    return render(request, 'about.html')

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # subject = request.POST.get('subject')
            # message = request.POST.get('message')
            # sender = request.POST.get('sender')
            # cc_myself = request.POST.get('cc_myself')

            # recipients = ['mesut8311006@gmail.com']

            # if cc_myself:
            #     recipients.append(sender)

            # send_mail(subject, message, sender, recipients, fail_silently=False)
            form.save()
        
    form = ContactForm()

    content = {
        "form": form,
    }
    return render(request, 'contact.html', content)

def products(request):
    kategoriler = EmlakTipi.objects.all()
    emlaklar = EmlakKayit.objects.filter(yayimla=True)


    content = {
        "kategoriler": kategoriler,
        "emlaklar": emlaklar,
    }
    return render(request, 'products.html', content)

def category(request, name):
    kategoriler = EmlakTipi.objects.all()
    emlaklar = EmlakKayit.objects.filter(yayimla=True, emlak_tipi__isim=name)

    content = {
        "kategoriler": kategoriler,
        "emlaklar": emlaklar,
    }
    return render(request, 'products.html', content)

def productdetails(request, id):
    product = get_object_or_404(EmlakKayit, id=id)
    images = []
    age = ""

    if product:
        images = EmlakKayitFoto.objects.filter(ev_kayit=id)

    if product.bina_yapım_yılı:
        # print(datetime.datetime.now().year)
        # print(str(product.bina_yapım_yılı).split("-")[0])
        age = int(datetime.datetime.now().year) - int(str(product.bina_yapım_yılı).split("-")[0])

    # print(age)
        
    content= {
        "product": product,
        "images": images,
        "age": age
    }
    return render(request, 'productdetail.html', content)