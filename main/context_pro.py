from .models import *

def view_all(request):
    context = {
        "categories": tag.objects.all(), 
        "products": product.objects.all()
    }
    return context 