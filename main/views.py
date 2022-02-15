from urllib import request
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required
import json
from .models import *
import telebot

TOKEN = '5261118959:AAFids6j-ivj-zv2gS5yE3yt9BkvVPXTby0'
bot = telebot.TeleBot(TOKEN)
user = "801531808"
# Create your views here.
def homeView(request):
    return render(request, "index.html",)
def menuView(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
def ProductDetailView(request,slug):
    food = Product.objects.select_related("category").get(slug=slug)
    related =  list(Product.objects.select_related("category").filter(category=food.category).values())
    return render(request, 'product.html', {'product': food, "related":related})


def Addcart(request):
    my = json.loads(request.GET["data"])
    d = []
    objects = list(Product.objects.select_related("category").filter(id=id_).values() for id_ in my)
    for i in objects:
        d +=i
    return JsonResponse({'success': d}) 
def card(request):
    # objects = [product.objects.select_related("category").get(id=id_) for id_ in my]
    return render(request, 'cart.html', )
    
def check(request):
    messages.info(request, mark_safe('Your request send'))
    a = json.loads(request.GET['data'])
    text = ''
    price = 0
    o = Order.objects.create(customer= a[0], tel = int(a[1]))
    for i in a[2]:
        products = Product.objects.get(id=i[0])
        c = Cart.objects.create(product=products, count = i[1])
        c.save()
        o.order.add(c)
        price += products.price * i[1]
        text += f'{ i[1]}ta {products.name} narxi: {products.price * i[1]}$ \n'
    o.text = (text)
    o.total = price
    o.save()
    bot.send_message(user, f"zakazchi: {a[0]},\n\n telefon nomeri: {a[1]}, \n\n buyurtma:\n {text} \n Total: {price}$  \n\n http://127.0.0.1:5000/superadmin/{o.id}")

    return JsonResponse({'success': 200}) 


@login_required(login_url="/login/")    
def superadmin(request):
    user = authenticate(username='safarbek',password='2007')
    if user.is_active:
        return render(request, 'superadmin/superadmin.html', {'orders': Order.objects.all()})
    else:
        return redirect("/login")


def checkorder(request):
    id = request.GET['data']
    a = Order.objects.get(id= id)
    a.is_arrived = True
    a.save()
    return JsonResponse({'success': 200}) 
@login_required(login_url="/login/")
def CheckView(request, num):
    order = Order.objects.get(id=num)
    return render(request, 'superadmin/customer.html', {'order': order})