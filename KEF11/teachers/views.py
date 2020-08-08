from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Subjects, Stats, Teachers, Query
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from .forms import StatsForm
import requests

# Create your views here.
def about(request):
	context={}
	return render(request,'teachers/about.html')

def teacherlogin(request):
	context={}
	return render(request,'teachers/teacherlogin.html')

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



def query(request):
	queries = Query.objects.all()
	context = {
		'queries': queries
	}
	return render(request, 'teachers/queries.html', context)


class QueryCreateView(CreateView):
	model = Query
	fields = ['teacher', 'title' , 'description']

	def form_valid(self, form):
	    form.instance.author = self.request.user
	    return super().form_valid(form)


class QueryDetailView(DetailView):
	model = Query


class QueryUpdateView(UpdateView):
	model = Query
	fields = ['teacher', 'title' , 'description']

	def form_valid(self, form):
	    form.instance.author = self.request.user
	    return super().form_valid(form)
	    

class QueryDeleteView(DeleteView):
	model = Query
	success_url = '/teachers/queries/'