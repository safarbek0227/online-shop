from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}

@admin.register(product)
class productAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}