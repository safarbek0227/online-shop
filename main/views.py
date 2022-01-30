from unicodedata import category
from urllib import request
from django.shortcuts import render
from django.template import context
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from datetime import datetime
import json
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
    global card
    card = json.loads(request.GET["data"])
    return JsonResponse({'success': 200}) 
def card(request):
    print(card)
    objects = [product.objects.get(id=id_) for id_ in card]
    return render(request, 'cart.html',{'pro' : objects})
    
def check(request):
    a = request.GET
    print(a)
    return render(request, "form.html",)


