from django import forms
from django.forms import ModelForm, TextInput
from .models import Stats


class StatsForm(ModelForm):

    class Meta:
        model = Stats
        fields = ['teacher', 'tutorials', 'subject']