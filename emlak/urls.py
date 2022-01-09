from django.urls import path
from .views import (
    home,
    about,
    contact,
    products,
    productdetails
)


urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('products/', products, name="products"),
    path('productdetails/<int:id>', productdetails, name="productdetails"),
]