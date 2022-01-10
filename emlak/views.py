import datetime
from django.shortcuts import get_object_or_404, render
from .models import (
    EmlakKayit,
    EmlakKayitFoto,
    MainSlider
    )

# Create your views here.

def home(request):
    evler = EmlakKayit.objects.filter(yayimla=True)
    slider = MainSlider.objects.all()
    # print(evler)
    content= {
        "evler":evler,
        "slider":slider
    }
    # print(content)
    return render(request, 'index.html', content)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def products(request):
    return render(request, 'products.html')

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