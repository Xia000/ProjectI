from django import forms
from .models import Employee
from django.core import validators


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'position', 'office', 'age', 'start_date', 'salary']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'office': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Name',
            'position': 'Position',
            'office': 'Office',
            'age': 'Age',
            'start_date': 'Start Date',
            'salary': 'Salary',
        }
        error_messages = {
            'name': {
                'required': 'Name is required',
            },
            'position': {
                'required': 'Position is required',
            },
            'office': {
                'required': 'Office is required',
            },
            'age': {
                'required': 'Age is required',
            },
            'start_date': {
                'required': 'Start Date is required',
            },
            'salary': {
                'required': 'Salary is required',
            },
        }
        validators = {
            'name': [validators.MinLengthValidator(2)],
            'position': [validators.MinLengthValidator(2)],
            'office': [validators.MinLengthValidator(2)],
            'age': [validators.MinLengthValidator(2)],
            'start_date': [validators.MinLengthValidator(2)],
            'salary': [validators.MinLengthValidator(2)],
        }
        


   