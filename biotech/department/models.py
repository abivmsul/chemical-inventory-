from django.db import models
from chemical.models import Chemical
# Create your models here.
from datetime import date


class AnimalStore(models.Model):
    temprature = (
        ('-', '-'),
        ('+4', '+4'),
        ('-20', '-20'),
        ('-80', '-80'),  
    )
    chemical = models.ForeignKey(Chemical, on_delete=models.DO_NOTHING)
    cabinate = models.CharField(max_length=100,default='-')
    shelf = models.CharField(max_length=100,default='-')
    available = models.IntegerField(default=0)
    recievedDate = models.DateTimeField(auto_now_add=True,null=True)
    expireDate = models.DateField(null=True)
    productionDate = models.DateField(null=True)
    temprature =  models.CharField(max_length=100, choices=temprature, default='-')
    def __str__(self):
        return self.chemical.name

    @property
    def expired(self):
        return date.today().year > self.expireDate.year
   
    @property
    def fresh(self):
        x = date.today().year
        y = self.expireDate.year
        fresh = x + ((y - x)/4)
        print(x,fresh,y,self.chemical)
        print("fresh")
        return date.today().year <= fresh    
    @property
    def ontheverge(self):
        a = date.today().year
        b = self.expireDate.year
        mid = a + ((b - a)/2)
        #print(a)
        print(a,mid,b,self.chemical)
        print("adf")
        return date.today().year <= mid

  


class PlantStore(models.Model):
    temprature = (
        ('-', '-'),
        ('+4', '+4'),
        ('-20', '-20'),
        ('-80', '-80'),  
    )
    chemical = models.ForeignKey(Chemical, on_delete=models.DO_NOTHING)
    cabinate = models.CharField(max_length=100,default='-')
    shelf = models.CharField(max_length=100,default='-')
    available = models.IntegerField(default=0)
    recievedDate = models.DateTimeField(auto_now_add=True, null=True)
    expireDate = models.DateField(null=True)
    temprature =  models.CharField(max_length=100, choices=temprature, default='-')
    def __str__(self):
        return self.chemical.name


class MicrobialStore(models.Model):
    temprature = (
        ('-', '-'),
        ('+4', '+4'),
        ('-20', '-20'),
        ('-80', '-80'),  
    )
    chemical = models.ForeignKey(Chemical, on_delete=models.DO_NOTHING)
    cabinate = models.CharField(max_length=100,default='-')
    shelf = models.CharField(max_length=100,default='-')
    available = models.IntegerField(default=0)
    recievedDate = models.DateTimeField(auto_now_add=True,null=True)
    expireDate = models.DateField(null=True)
    temprature =  models.CharField(max_length=100, choices=temprature, default='-')
    def __str__(self):
        return self.chemical.name



class AnimalDesposedChemical(models.Model):
    temprature = (
        ('-', '-'),
        ('+4', '+4'),
        ('-20', '-20'),
        ('-80', '-80'),  
    )
    chemical = models.ForeignKey(Chemical, on_delete=models.DO_NOTHING)
    cabinate = models.CharField(max_length=100)
    shelf = models.CharField(max_length=100)
    available = models.IntegerField(default=0)
    recievedDate = models.DateTimeField(auto_now_add=True,null=True)
    expireDate = models.DateField(null=True)
    desposedDate = models.DateField(null=True)
    desposed = models.BooleanField(default=False)
    temprature =  models.CharField(max_length=100, choices=temprature, default='-')

    def __str__(self):
        return self.chemical.name

class PlantDesposedChemical(models.Model):
    temprature = (
        ('-', '-'),
        ('+4', '+4'),
        ('-20', '-20'),
        ('-80', '-80'),  
    )
    chemical = models.ForeignKey(Chemical, on_delete=models.DO_NOTHING)
    cabinate = models.CharField(max_length=100)
    shelf = models.CharField(max_length=100)
    available = models.IntegerField(default=0)
    recievedDate = models.DateTimeField(auto_now_add=True,null=True)
    expireDate = models.DateField(null=True)
    desposedDate = models.DateField(null=True)
    desposed = models.BooleanField(default=False)
    temprature =  models.CharField(max_length=100, choices=temprature, default='-')
    def __str__(self):
        return self.chemical.name

class MicrobialDesposedChemical(models.Model):
    temprature = (
        ('-', '-'),
        ('+4', '+4'),
        ('-20', '-20'),
        ('-80', '-80'),  
    )
    chemical = models.ForeignKey(Chemical, on_delete=models.DO_NOTHING)
    cabinate = models.CharField(max_length=100)
    shelf = models.CharField(max_length=100)
    available = models.IntegerField(default=0)
    recievedDate = models.DateTimeField(auto_now_add=True,null=True)
    expireDate = models.DateField(null=True)
    desposedDate = models.DateField(null=True)
    desposed = models.BooleanField(default=False)
    temprature =  models.CharField(max_length=100, choices=temprature, default='-')
    def __str__(self):
        return self.chemical.name