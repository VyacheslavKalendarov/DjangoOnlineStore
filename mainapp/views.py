from django.shortcuts import render

def index(request):
    context = {
        'page_title': 'главная'
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {
        'page_title': 'каталог'
    }
    return render(request, 'mainapp/products.html', context)

def contact(request):
    locations = [
        {'city': 'Москва',
         'phone': '+7-888-333-7777',
         'email': 'info@geekshop.ru',
         'address': 'В пределах МКАД'},
        {'city': 'Санкт-Петербург',
         'phone': '+7-888-222-8888',
         'email': 'info.spb@geekshop.ru',
         'address': 'В пределах КАД'},
        {'city': 'Хабаровск',
         'phone': '+7-888-444-8888',
         'email': 'info.east@geekshop.ru',
         'address': 'В пределах центра'},
    ]

    context = {
        'page_title': 'контакты',
        'locations': locations
    }
    return render(request, 'mainapp/contact.html', context)

