from django.urls import path
from .import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = "main"
urlpatterns = [
    path('', views.homeView, name="index"),
    path('menu/', views.menuView, name="index"),
    path('about/', views.about, name="about"),
    path("detail/<slug>", views.ProductDetailView, name='detail'),
    path('card/', views.card, name='card'),
    path('check/', views.check, name='card'),
    path("addcard/", views.Addcart, name='detail'),
    path("login/",  LoginView.as_view(template_name="superadmin/login.html", success_url="/superadmin/"),name="login"),
    path("logout/", LogoutView.as_view(template_name="superadmin/logout.html"),name="logout"),
    path("superadmin/", views.superadmin, name='superadmin'),
    path("checkadmin/", views.checkorder, name='superadmin'),
    path("superadmin/<int:num>", views.CheckView, name='superadmin'),
]