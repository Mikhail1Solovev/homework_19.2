from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'catalog/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # Обработка данных формы (например, сохранение в базу данных)
        return HttpResponse('Спасибо за ваше сообщение!')
    return render(request, 'catalog/contacts.html')
