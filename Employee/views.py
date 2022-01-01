from django.shortcuts import render, HttpResponseRedirect
from Employee import models
from Employee.models import Employee
from .forms import EmployeeForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def show_employee(request):
    show_employee = models.Employee.objects.all()
    return render(request, 'show_employee.html', {'show_employee': show_employee})

def create(request):
    if request.method == 'POST':
        fm = EmployeeForm(request.POST)   
        if fm.is_valid():
            name = fm.cleaned_data['name']
            position = fm.cleaned_data['position']
            office = fm.cleaned_data['office']
            age = fm.cleaned_data['age']
            start_date = fm.cleaned_data['start_date']
            salary = fm.cleaned_data['salary']
            reg = models.Employee(name=name, position=position, office=office, age=age, start_date=start_date, salary=salary)
            reg.save()
            fm = EmployeeForm()
    else:
        fm = EmployeeForm()
    emp = Employee.objects.all()
    return render(request, 'create.html', {'form': fm, 'employee': emp})


# Delete Data

def delete(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return HttpResponseRedirect('/create/')

# def edit(request, id ):
#     return render(request, 'update.html' , {'id': id})



def edit(request, id):
    
    if request.method == 'POST':
        pi = Employee.objects.get(id=id)
        fm = EmployeeForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/create/')
    else:
        pi = Employee.objects.get(id=id)
        fm = EmployeeForm(instance=pi)
    return render(request, 'update.html', {'form': fm})