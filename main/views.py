from urllib import request
from django.shortcuts import render,redirect
from django.template import context
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from datetime import datetime
import json
from .models import *
import telebot

TOKEN = '5092916545:AAElg9jee_ZMmtNoAqKqGAR5vQ0GqtIEf6k'
bot = telebot.TeleBot(TOKEN)
user = 801531808
bot.send_message(user, f"site iso online")
# Create your views here.
def homeView(request):
    return render(request, "index.html",)
def menuView(request):
    return render(request, "home.html")

def ProductDetailView(request,slug):
    food = product.objects.select_related("category").get(Slug=slug)
    related =  list(product.objects.select_related("category").filter(category=food.category).values())
    return render(request, 'product.html', {'product': food, "related":related})

global my
my = []
def Addcart(request):
    global my
    my = json.loads(request.GET["data"])
    return JsonResponse({'success': 200}) 
def card(request):
    objects = [product.objects.select_related("category").get(id=id_) for id_ in my]
    return render(request, 'cart.html', {'pro': objects})
    
def check(request):
    a = json.loads(request.GET['data'])
    bot.send_message(user, f"zakazchi: {a[0]},\n\n telefon nomeri: {a[1]}, \n\n buyurtma: \n\n {a[2]}")
    return redirect("/card/")


