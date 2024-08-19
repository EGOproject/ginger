from django.shortcuts import render, get_object_or_404
from items.models import Category, Item

def preview(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'core/preview.html', {'item': item})