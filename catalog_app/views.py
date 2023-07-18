from django.shortcuts import render
from catalog_app.models import Product


# Create your views here.
def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')


def product(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Продукты'
    }
    return render(request, 'catalog/product.html', context)
