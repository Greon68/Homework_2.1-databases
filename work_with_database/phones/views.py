from django.shortcuts import render, redirect
from django.http import HttpResponse

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones = Phone.objects.all()
    template = 'catalog.html'
    sort = request.GET.get('sort','')
    if sort:
        if sort == 'min_price':
            sort = 'price'
        if sort == 'max_price':
            sort = '-price'
        phones = phones.order_by(sort)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone':phone}
    return render(request, template, context)

# Дополнение преподователя:
# " Обратите внимание. Менять порядок отображения товаров
# в каталоге можно более простым способом" :

def show_catalog_2(request):
    SORT_MAP = {
    'name': 'name',
    'min_price': 'price',
    'max_price': '-price',
    }
    phones = Phone.objects.all()
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort:
        phones = phones.order_by(SORT_MAP[sort])
    context = {'phones': phones}
    return render(request, template, context)





