from django.shortcuts import render,redirect
from employee.models import Assign,Employee
from Schools.models import UnregisteredSchools
from employee.forms import RegistrationForm,SchoolForm


# Create your views here.
def requests(request):
    employees=Employee.objects.all()
    schools=UnregisteredSchools.objects.all()
    
    if request.method=='POST':
        employee_name=request.POST['employee_name']
        school_name=request.POST['school_name']
        r=Assign.objects.create(employee_name=employee_name,school_name=school_name)
        r.save()
        return redirect('requests')

    return render(request,'requests.html',{'employees':employees,'schools':schools})
