from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def products(request):
    return render(request, 'products.html')

def productdetails(request, id):
    content= {
        id: id,
    }
    return render(request, 'productdetail.html', content)