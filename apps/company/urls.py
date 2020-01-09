from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views


app_name = 'company'

urlpatterns = [
    path('employees/',
         login_required(views.EmployeeList.as_view()), name='employees-list'),
    path('departments/',
         login_required(views.DepartmentsList.as_view()), name='departments-list'),
    path('net_devices/',
         login_required(views.NetDevices.as_view()), name='net_devices'),
]
