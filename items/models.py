from django.db import models

# Create your models here
from django.urls import reverse


class Warehouse(models.Model):
    country = models.CharField(max_length=250)
    town = models.CharField(max_length= 250)

    def __str__(self) -> str:
        return f'{self.country},{self.town}'

    def get_absolute_url(self):
        return reverse('location_detail', args=[str(self.id)])
    

class Item(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item_detail', args=[str(self.id)])
