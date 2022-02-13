from .models import *

def view_all(request):
    context = {
        "categories": Tag.objects.all(), 
        "products": Product.objects.select_related("category").all()
    }
    return context 