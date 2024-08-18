from django.shortcuts import render
from items.models import Category, Item
from random import shuffle

def index(request):
    items = list(Item.objects.filter(available=True))
    shuffle(items)  # Randomize the order of items
    categories = Category.objects.all()
    
    # Group items by categories for easy access in the template
    categorized_items = {}
    for category in categories:
        categorized_items[category.name] = list(category.items.filter(available=True))

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,  # [:6] Display first 6 randomized items
        'categorized_items': categorized_items,
    })


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