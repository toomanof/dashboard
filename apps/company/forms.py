from django import forms

from django_select2.forms import ModelSelect2Widget

from ..localset.models import RegisteredHost
from .models import Employee, Departments, NetDevices


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'patronymic', 'surname', 'phone', 'department',)
        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
            'department': forms.Select(attrs={'required': True}),
        }


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
        }


class NetDevicesForm(forms.ModelForm):
    

    class Meta:
        model = NetDevices
        fields = ('name', 'employee', 'department', 'host',)
        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
             'employee': forms.Select(attrs={'required': True}),
            'department': forms.Select(attrs={'required': True}),
            'host': forms.Select(attrs={'required': True})
        }
