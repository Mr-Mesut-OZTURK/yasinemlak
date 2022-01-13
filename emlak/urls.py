from django.urls import path
from .views import (
    home,
    about,
    contact,
    products,
    productdetails,
    category
)


urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('products/', products, name="products"),
    path('products/<str:name>', category, name="category"),
    path('productdetails/<int:id>', productdetails, name="productdetails"),
]