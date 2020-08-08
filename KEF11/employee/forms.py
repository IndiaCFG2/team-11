from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Schools.models import Schools

class RegistrationForm(UserCreationForm):
	email=forms.EmailField()
	class Meta:
		model=User
		fields=['username','email','password1','password2',]



class SchoolForm(forms.ModelForm):
    class Meta:
        model=Schools
        fields='__all__'



