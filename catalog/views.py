from django.shortcuts import render
from .models import Product, Contact

def home(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    for product in latest_products:
        print(product.name)
    return render(request, 'home.html', {'latest_products': latest_products})

def contacts(request):
    contact = Contact.objects.first()
    return render(request, 'contacts.html', {'contact': contact})
