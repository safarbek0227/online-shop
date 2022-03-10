from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import SlugField
from django.shortcuts import reverse
# from accounts.models import Profile
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Tag(models.Model):
    name = models.CharField('categoriya nomi', max_length=25)
    slug = models.SlugField('*', max_length=25)

    class Meta:
        ordering = ["id"]
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField('nomi', max_length=25)
    slug = models.SlugField('*', max_length=25)
    image = models.ImageField("Product image", upload_to='product_images/')
    category = models.ForeignKey(Tag, on_delete=CASCADE)
    price = models.PositiveIntegerField("Price", default=0)
    description = models.TextField("About product")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
        unique_together = ["slug"]
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=CASCADE)
    count = models.PositiveIntegerField('soni',default=0)
    def __str__(self):
        return self.product.name


class Order(models.Model):
    customer = models.CharField('buyurtmachi', max_length=25)
    tel = models.PositiveIntegerField('tel', default=0)
    order = models.ManyToManyField(Cart)
    text = models.TextField('*')
    total = models.PositiveIntegerField(default=0)
    is_arrived = models.BooleanField(default=False)
    class Meta:
        ordering = ["-id"]
    def __str__(self):
        return self.customer