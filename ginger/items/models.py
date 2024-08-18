from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',) # alphabetical order
        verbose_name_plural = 'Categories' # for plural adjust
    
    def __str__(self):
        return self.name.capitalize()        # return actual names of fields in table


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    item_img1 = models.ImageField(upload_to='item_images', blank=True, null=True)
    item_img2 = models.ImageField(upload_to='item_images', blank=True, null=True)
    item_img3 = models.ImageField(upload_to='item_images', blank=True, null=True)
    available = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name        # return actual names of fields in table
