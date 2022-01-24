from urllib import request
from django.shortcuts import render
# from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect,JsonResponse
from .models import *
# Create your views here.

def homeView(request):
    return render(request, "index.html",)
def menuView(request):
    return render(request, "home.html")

def ProductDetailView(request,slug):
    food = product.objects.get(Slug=slug)
    related =  list(product.objects.filter(category=food.category).values())
    return render(request, 'product.html', {'product': food, "related":related})

def Addcart(request):
    d = request.GET.get('data')
    cart = product.objects.get(id=d)
    print(cart.price)
    return JsonResponse({'success': 200})
