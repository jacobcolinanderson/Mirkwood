from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    race = models.CharField(max_length=100, blank=False, default='')
    personality = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    description = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.name