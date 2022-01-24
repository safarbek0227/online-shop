from django.urls import path
from .import views

app_name = "main"
urlpatterns = [
    path('', views.homeView, name="index"),
    path('menu/', views.menuView, name="index"),
    path("detail/<slug>", views.ProductDetailView, name='detail'),
    path("AddCart/", views.Addcart, name='detail')
]