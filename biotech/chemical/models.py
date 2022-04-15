from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chemical(models.Model): 
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=30)
    company = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    #expireDate = models.DateField()
    
    def __str__(self):
        return self.name

class RequestChemical(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    requested = models.BooleanField(default=False)
    chemical = models.ForeignKey(Chemical, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    issuedquantity = models.IntegerField(default=0)
    recieved = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.quantity} of {self.chemical.name}"


class Request(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # ref_code = models.CharField(max_length=20, blank=True, null=True)
    chemicals = models.ManyToManyField(RequestChemical)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    requested = models.BooleanField(default=False)
    department = models.CharField(max_length=100, null=True)
    # shipping_address = models.ForeignKey(
    #     'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    deptRequest = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    deny = models.BooleanField(default=False)
    checked = models.BooleanField(default=False)
    pin = models.CharField(max_length=4)

    class Meta:
        ordering = ['-ordered_date' ,'-received']
    
    def __str__(self):
        return self.user.username



