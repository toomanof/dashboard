from django.http import Http404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Employee, Departments, NetDevices
from .serializers import EmployeeSerializer, DepartmentsSerializer, NetDevicesSerializer


class ApiEmployees(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ApiDepartments(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer

class ApiNetDevices(viewsets.ModelViewSet):
    queryset = NetDevices.objects.all()
    serializer_class = NetDevicesSerializer
