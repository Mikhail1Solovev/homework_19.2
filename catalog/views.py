from django.shortcuts import render, HttpResponse
from .models import Product, Contact

def home(request):
    products = Product.objects.order_by('-created_at')[:5]
    for product in products:
        print(product.name)
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return HttpResponse('Thank you for your message!')
    else:
        contacts = Contact.objects.all()
        return render(request, 'catalog/contacts.html', {'contacts': contacts})
