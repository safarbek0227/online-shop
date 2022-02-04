from urllib import request
from django.shortcuts import render,redirect
from django.template import context
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from datetime import datetime
import json
from .models import *
import telebot

TOKEN = 'yur bot token'
bot = telebot.TeleBot(TOKEN)
user = 801531808
bot.send_message(user, f"site iso online")
# Create your views here.
def homeView(request):
    return render(request, "index.html",)
def menuView(request):
    return render(request, "home.html")

def ProductDetailView(request,slug):
    food = product.objects.select_related("category").get(slug=slug)
    related =  list(product.objects.select_related("category").filter(category=food.category).values())
    return render(request, 'product.html', {'product': food, "related":related})


def Addcart(request):
    my = json.loads(request.GET["data"])
    d = []
    objects = list(product.objects.select_related("category").filter(id=id_).values() for id_ in my)
    for i in objects:
        d +=i
    return JsonResponse({'success': d}) 
def card(request):
    # objects = [product.objects.select_related("category").get(id=id_) for id_ in my]
    return render(request, 'cart.html', )
    
def check(request):
    a = json.loads(request.GET['data'])
    text = ''
    for i in a[2]:
        products = product.objects.get(id=i[0])
        text += f'{ i[1]}ta \n {products.name} \n narxi: {products.price}\n jami: {products.price * i[1]} \n \n'
    bot.send_message(user, f"zakazchi: {a[0]},\n\n telefon nomeri: {a[1]}, \n\n buyurtma:\n {text}")
    return redirect("/card/")


