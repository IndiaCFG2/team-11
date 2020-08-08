



from django.shortcuts import render,redirect,get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from Schools.models import Schools
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import RegistrationForm
from django.http import HttpResponse, Http404
from django.contrib.auth import login,logout
# Create your views here.
from employee.models import Employee,Users,Assign
from django.utils import timezone
import datetime


def home(request):
    recievedrequests=Assign.objects.all()

    return render(request,'home.html',{'recievedrequests':recievedrequests})



def map(request):
    mapbox_access_token = 'pk.eyJ1Ijoic3JpZGhhcjAwMDciLCJhIjoiY2s3b2lra3N4MDVyNzNmbXNsZGZsY2htdiJ9.QGZpr-aeWNBms5QBmdHEUA'
    return render(request, 'map.html',
                  { 'mapbox_access_token': mapbox_access_token })


def list_schools(request):
    user=User.objects.first()
    schools=user.schools_set.all()

    return render(request,'list_schools.html',{'schools':schools})


def register_school(request):
    if request.method=='POST':
        school_name=request.POST['schoolname']
        email=request.POST['email']
        phonenumber= 98899877
        headmaster=request.POST['headmaster']


        send_mail('KFSFOUNDATION','Hello {} thanks for registering'.format(school_name),'kfsngo@gmail.com',[email],fail_silently=False,)
        school=Schools.objects.create(employee=request.user,name=school_name,phone=phonenumber,email=email,headmaster=headmaster)
        school.save()
        p=Users(useremail=email)
        p.save()

        return redirect('/home')

    return render(request,'employee/school_register.html')

def register_employee(request):
    form=RegistrationForm()
    error=None
    if request.method=="POST":
        emai=request.POST.get('email')
        try:
            a=Users.objects.get(useremail=emai)
        except Users.DoesNotExist :
            return HttpResponse("NOt validated")

        form1=RegistrationForm(request.POST)
        if form1.is_valid() :
            userr=form1.save()


            return redirect("/login")
        return render(request,"employee/register.html",{'err':form1.errors})
    return render(request,"employee/register.html",{'form':form})











def list_schools(request):
    user=User.objects.first()
    if request.method =='POST':
        name=request.POST['search']


        if user.schools_set.filter(name=name)!=None:
            schools=user.schools_set.filter(name=name)
            return render(request,'list_schools.html',{'schools':schools,'t':1})
        elif user.schools_set.filter(headmaster=name) != None:
            schools=user.schools_set.filter(headmaster=name)
            return render(request,'list_schools.html',{'schools':schools,'t':2})


    schools=user.schools_set.all()

def delete(request,id1):
    f=Schools.objects.filter(id=id1)
    if request.method=="POST":
        try:
            instance=Schools.objects.get(pk=id1)
            instance.delete()
            return redirect('/manager/')
        except:
            return HttpResponse(status=404)
    return render(request,"employee/delete.html",{'form':f})


def login_asview(request):
    form=AuthenticationForm()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        form=AuthenticationForm(data=request.POST)

        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('/home')
        else:
            return render(request,'employee/login.html',{'form':form})

    else:
        return render(request,'employee/login.html',{'form':form})


def logout_asview(request):
    logout(request)
    return redirect('/')


def requests(requets):
    if request.method=='POST':
        employee_name=request.POST['employee_name']
        school_name=request.POST['school_name']
        r=Requests(employee_name=employee_name,school_name=school_name)
        return redirect('/requests')

    return render(request,'requests.html')
