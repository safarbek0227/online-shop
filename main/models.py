from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import SlugField
from django.shortcuts import reverse
# from accounts.models import Profile
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class tag(models.Model):
    name = models.CharField('categoriya nomi', max_length=25)
    slug = models.SlugField('*', max_length=25)

    class Meta:
        ordering = ["id"]
    def __str__(self):
        return self.name
    
class product(models.Model):
    name = models.CharField('nomi', max_length=25)
    Slug = models.SlugField('*', max_length=25)
    image = models.ImageField("Product image", upload_to='product_images/')
    category = models.ForeignKey(tag, on_delete=CASCADE)
    price = models.PositiveIntegerField("Price", default=0)
    description = models.TextField("About product")

    def __str__(self):
        return self.name