from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *




class RegisterUserForm(UserCreationForm):
	username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
	email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input'}))
	password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-input'}))
	password2 = forms.CharField(label='Повтор пароля', widget=forms.TextInput(attrs={'class': 'form-input'}))


	






	class Metf:
		model = User
		fields = {'username', 'email', 'password1', 'password2'}



class LoginUserForm(AuthenticationForm):
	username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
	password = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-input'}))




class ContactForm(forms.Form):
	name =  forms.CharField(label='Имя', max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
	email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input'}))
	contact = forms.CharField(widget=forms.Textarea(attrs={'cols': 20, 'rows': 10, 'class': 'form-input'}))
	captcha = CaptchaField()
