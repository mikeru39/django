from django.shortcuts import render

from django.shortcuts import get_object_or_404
from .models import ProductCategory, Product
# Create your views here.
def main(request):
    products = Product.objects.all()[:6]
    content = {'title': "Itnterior", 'products': products}
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
