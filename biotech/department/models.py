from django.db import models
from chemical.models import Chemical
# Create your models here.

class AnimalStore(models.Model):
    chemical = models.ForeignKey(Chemical, on_delete=models.DO_NOTHING)
    cabinate = models.CharField(max_length=100)
    shelf = models.CharField(max_length=100)
    available = models.IntegerField(default=0)
    recievedDate = models.DateTimeField(auto_now_add=True,null=True)
    expireDate = models.DateField(null=True)

    def __str__(self):
        return self.chemical.name


class PlantStore(models.Model):
    chemical = models.ForeignKey(Chemical, on_delete=models.DO_NOTHING)
    cabinate = models.CharField(max_length=100)
    shelf = models.CharField(max_length=100)
    available = models.IntegerField(default=0)
    recievedDate = models.DateTimeField(auto_now_add=True, null=True)
    expireDate = models.DateField(null=True)
    def __str__(self):
        return self.chemical.name


class MicrobialStore(models.Model):
    chemical = models.ForeignKey(Chemical, on_delete=models.DO_NOTHING)
    cabinate = models.CharField(max_length=100)
    shelf = models.CharField(max_length=100)
    available = models.IntegerField(default=0)
    recievedDate = models.DateTimeField(auto_now_add=True,null=True)
    expireDate = models.DateField(null=True)
    def __str__(self):
        return self.chemical.name
