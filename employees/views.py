from django.shortcuts import render, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

#decide which urls patterns to create
#Created URL ptterns in the main urls.py, and forward i to employees.urls
#Created the template
# Create your views here.
def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)

    context = {
        'employee': employee
    }
    return render(request, 'employee_detail.html', context)


def add_employee(requets):
    if requets.method == 'POST':
        form = EmployeeForm(requets.POST, requets.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    form = EmployeeForm()
    context = {
       'form' : form,
   }
    return render(requets, 'add_employee.html', context)
    