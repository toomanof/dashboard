from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import RegisteredHostForm, OnLineHostForm

from apps.mixins import MixinDinamicTablesView


class OnLineHost(MixinDinamicTablesView, FormView):
    form_class = OnLineHostForm
    table_title = title = 'On-line хосты'
    data_ajax_url = reverse_lazy('api_localset:clients_online-list')
    readonly = True
    columns_name = [
        'IP', 'MAC', 'Производитель', 'Active host',]


class RegisteredHostView(MixinDinamicTablesView, FormView):
    form_class = RegisteredHostForm
    table_title = title = 'Хосты сетевых устройств'
    data_ajax_url = reverse_lazy('api_localset:reg_hosts_dhcp-list')
    columns_name = ['IP', 'MAC', 'Host name', 'Sub mask', 'Routers', 'DNS']
