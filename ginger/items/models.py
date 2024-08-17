from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',) # alphabetical order
        verbose_name_plural = 'Categories' # for plural adjust
    
    def __str__(self):
        return self.name.capitalize()        # return actual names of fields in table


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()