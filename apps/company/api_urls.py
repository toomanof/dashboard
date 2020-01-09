from django.urls import path, include

from rest_framework import routers

from . import api_views

app_name = 'api_company'

router = routers.DefaultRouter()
router.register('employees', api_views.ApiEmployees, 'employees')
router.register('departments', api_views.ApiDepartments, 'departments')
router.register('net_devices', api_views.ApiNetDevices, 'net_devices')


urlpatterns = [
    path('', include(router.urls)),
]
