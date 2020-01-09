from django.db import models

from ..localset.models import RegisteredHost


class Departments(models.Model):
    name = models.CharField('Название', max_length=250, help_text='Введите назваине')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField('Название', max_length=250, help_text='Введите назваине')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField('Имя', max_length=100)
    patronymic = models.CharField('Отчество', max_length=250,
                                  null=True, blank=True)
    surname = models.CharField('Фамилия', max_length=250)
    nickname = models.CharField('Обращение', max_length=250,
                                  null=True, blank=True)
    phone = models.CharField('Телефон', max_length=30,
                             null=True, blank=True,)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE,
                                   verbose_name='Отдел',
                                   null=True, blank=True,
                                   related_name='employees')
    position = models.ForeignKey(Position, on_delete=models.CASCADE,
                                 verbose_name='Должность',
                                 null=True, blank=True,
                                 related_name='employees')

    def __str__(self):
        return f'{self.name} {self.patronymic} {self.surname}'


class NetDevices(models.Model):
    name = models.CharField('Имя', max_length=250)
    employee = models.ForeignKey(
        Employee, verbose_name='Сотрудник', on_delete=models.CASCADE,
        null=True, blank=True, related_name='net_devices')
    department = models.ForeignKey(
        Departments, verbose_name='Отдел', on_delete=models.CASCADE,
        null=True, blank=True, related_name='net_devices')
    host = models.ForeignKey(
        RegisteredHost, verbose_name='Зарегистрированный хост',
        on_delete=models.CASCADE,
        null=True, blank=True, related_name='net_devices')

    def __str__(self):
        return f'"{self.name}" {self.employee} ip:{self.host}'

    @property
    def department_name(self):
        return self.department.name

    @property
    def employee_name(self):
        return self.employee.name

    @property
    def host_ip(self):
        return self.host.ip
