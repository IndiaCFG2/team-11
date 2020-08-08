from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Subjects, Stats, Teachers
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from .forms import StatsForm
import requests

# Create your views here.

def teacher(request):
    teachers = Teachers.objects.all()
    context = {
        'teachers': teachers
    }
    return render(request, 'teachers/teachers.html', context)



def tutorial(request):
    response = requests.get('https://sheetdb.io/api/v1/gb2weo7rv3acv')
    print(response.content)
    form = StatsForm
    context = { 'form': form }
    return render(request, 'teachers/tutorials.html', context)



def test(request):
    context = {}
    return render(request, 'teachers/test.html', context)