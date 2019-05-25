from django.shortcuts import get_object_or_404
from django.shortcuts import render
import random
from .models import ProductCategory, Product
from basketapp.models import Basket


def main(request, pk=None):
    hot_products = Product.objects.filter(is_hot=True).first()
    content = {'title': "Itnterior", 'hot_products': hot_products}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('category')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('category')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
        }

        return render(request, 'mainapp/products.html', content)

    same_products = Product.objects.all()

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    products = Product.objects.all()[:6]
    content = {'title': "Contact", 'products': products}
    return render(request, 'mainapp/contact.html', content)

def description(request, pk):
    content = {
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),

    }

    return render(request, 'mainapp/description.html', content)




def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category). \
                        exclude(pk=hot_product.pk)[:3]

    return same_products

