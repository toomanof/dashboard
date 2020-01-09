from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from apps.mixins import MixinDinamicTablesView

from .forms import EmployeeForm, DepartmentForm, NetDevicesForm


class EmployeeList(MixinDinamicTablesView, FormView):
    form_class = EmployeeForm
    table_title = title = 'Сотрудники'
    data_ajax_url = reverse_lazy('api_company:employees-list')
    columns_name = ['Имя', 'Отчество', 'Фамилия', 'Обращение', 'Телефон','Должность', 'Отдел']
    fields_name = ['name','patronymic', 'surname', 'nickname', 'phone', 'position', 'department']


class DepartmentsList(MixinDinamicTablesView, FormView):
    form_class = DepartmentForm
    table_title = title = 'Отделы'
    data_ajax_url = reverse_lazy('api_company:departments-list')
    columns_name = ['Названия']
    fields_name = ['name']


class NetDevices(MixinDinamicTablesView, FormView):
    form_class = NetDevicesForm
    table_title = title = 'Привязка сетевых устройств'
    data_ajax_url = reverse_lazy('api_company:net_devices-list')
    columns_name = ['Названия', 'Сотрудник','Отдел', 'Хост']
    fields_name = ['name', 'employee_name', 'department_name', 'host_ip']
    
