from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','username', 'password1', 'password2']
		#fields = '__all__'

class UpdateForm(ModelForm):
	class Meta:
		model = User_profile
		fields = '__all__'
		#fields = '__all__'

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['text','image']
		#fields = '__all__'
