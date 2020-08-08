from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from Schools.models import Schools
from django.contrib.auth.models import User,auth

# Create your views here.

def register_school(request):
    if request.method=='POST':
        school_name=request.POST['schoolname']
        email=request.POST['email']
        phonenumber= 98899877
        headmaster=request.POST['headmaster']
        

        send_mail('KFSFOUNDATION','Hello {} thanks for registering'.format(school_name),'kfsngo@gmail.com',[email],fail_silently=False,)
        school=Schools.objects.create(employee=request.user,name=school_name,phone=phonenumber,email=email,headmaster=headmaster)
        school.save()

        return redirect("/")

    return render(request,'school_register.html')



def home(request):

    return render(request,'home.html')



def map(request):
    mapbox_access_token = 'pk.eyJ1Ijoic3JpZGhhcjAwMDciLCJhIjoiY2s3b2lra3N4MDVyNzNmbXNsZGZsY2htdiJ9.QGZpr-aeWNBms5QBmdHEUA'
    return render(request, 'map.html',
                  { 'mapbox_access_token': mapbox_access_token })


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

    return render(request,'list_schools.html',{'schools':schools})







def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid login details')
            return redirect('login.html')

    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
