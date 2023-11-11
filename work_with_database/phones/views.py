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



