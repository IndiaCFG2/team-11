from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from Schools.models import Schools
from django.contrib.auth.models import User

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

        return redirect('employee/normal.html')

    return render(request,'employee/school_register.html')



def home(request):

    return render(request,'employee/normal.html')



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
            return redirect('employee/login.html')

    else:
        return render(request,'employee/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
