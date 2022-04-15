from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from chemical.models import Chemical
from department.models import *


class AddChemicalForm(ModelForm):
	class Meta:
		model = Chemical
		fields = ['name','company','description','unit']
		
class Atemp(ModelForm):
	class Meta:
		model = AnimalStore
		fields = ['temprature']

class Ptemp(ModelForm):
	class Meta:
		model = PlantStore
		fields = ['temprature']

class Mtemp(ModelForm):
	class Meta:
		model = MicrobialStore
		fields = ['temprature']