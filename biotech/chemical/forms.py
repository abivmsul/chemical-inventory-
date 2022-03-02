from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from chemical.models import Chemical

class AddChemicalForm(ModelForm):
	class Meta:
		model = Chemical
		fields = ['name','company','description','unit']
		
