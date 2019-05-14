from django.shortcuts import render
from .models import ProductCategory, Product
# Create your views here.
def main(request):
    products = Product.objects.all()[:6]
    content = {'title': "Itnterior", 'products': products}
    return render(request, 'mainapp/index.html', content)


def products(request):
    products = Product.objects.all()[:6]
    content = {'title': "Products", 'products': products}
    return render(request, 'mainapp/products.html', content)


def contact(request):
    products = Product.objects.all()[:6]
    content = {'title': "Contact", 'products': products}
    return render(request, 'mainapp/contact.html', content)
