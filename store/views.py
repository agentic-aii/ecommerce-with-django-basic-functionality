from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home(request):
    
    products = Product.objects.all()
    
    html_template = "store/home.html"
    
    context = {
        'products': products
    }

    return render(request, html_template, context)
