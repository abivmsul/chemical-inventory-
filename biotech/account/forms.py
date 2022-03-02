from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email']
		

class ResearcherForm(ModelForm):
	class Meta:
		model = Researcher
		fields = ['department']
		exclude = ['user']


class DeptForm(ModelForm):
	class Meta:
		model = Department
		fields = ['department']
		exclude = ['user']


