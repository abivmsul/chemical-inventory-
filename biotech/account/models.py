from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Researcher(models.Model):

    Department = (
        ('Microbial Biotechnology', 'Microbial Biotechnology'),
        ('Animal Biotechnology', 'Animal Biotechnology'),
        ('Plant Biotechnology', 'Plant Biotechnology'),  
    )
    
    researcher = models.OneToOneField(User, null=True, on_delete=models.CASCADE )
    name = models.CharField(max_length=100, null=True)
    department =  models.CharField(max_length=100, choices=Department, default='-')
    permission = models.BooleanField(default=False)
    def __str__(self):
		    return self.name

class Custodian(models.Model):
    custodian = models.OneToOneField(User,null= True, on_delete = models.CASCADE)
    name = models.CharField(max_length= 100 ,null= True)
    phone = models.IntegerField(null= True)

    def __str__(self):
		    return self.name

class Department(models.Model):
    Department = (
        ('Microbial Biotechnology', 'Microbial Biotechnology'),
        ('Animal Biotechnology', 'Animal Biotechnology'),
        ('Plant Biotechnology', 'Plant Biotechnology'),  
    )
    departments = models.OneToOneField(User,null= True, on_delete = models.CASCADE)
    name = models.CharField(max_length= 100 ,null= True)
    phone = models.IntegerField(null= True)
    department =  models.CharField(max_length=100, choices=Department, default='-')
    
    def __str__(self):
		    return self.name


class Director(models.Model):
    director = models.OneToOneField(User,null= True, on_delete = models.CASCADE)
    name = models.CharField(max_length= 100 ,null= True)
    phone = models.IntegerField(null= True)

    def __str__(self):
		    return self.name
