from django.shortcuts import render

# Create your views here.
def main(request):
    content = {'title': "Interior"}
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = {'title': "Products"}
    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = {'title': "Contact"}
    return render(request, 'mainapp/contact.html', content)
