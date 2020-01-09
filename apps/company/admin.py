from django.contrib import admin

from .models import Departments, Position, Employee, NetDevices


@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'patronymic',
        'surname', 'nickname', 'phone', 'department', 'position')

@admin.register(NetDevices)
class NetDevicesAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'employee', 'host',)