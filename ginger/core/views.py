from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

def orders(request):
    return render(request, 'core/orders.html')

def cart(request):
    return render(request, 'core/cart.html')

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')