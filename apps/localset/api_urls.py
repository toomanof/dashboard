from django.urls import path, include

from rest_framework import routers

from . import api_view

app_name = 'api_localset'

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('reg_hosts', api_view.ApiHostsInDhcpServer, 'reg_hosts_dhcp')
router.register(
    'api_clients_online', api_view.ApiClientOnline, 'clients_online')

reg_clients = api_view.ApiUnknow_clients.as_view()
clients_online_count = api_view.ApiCountClientOnline.as_view()


urlpatterns = [
    path('', include(router.urls)),
    path('reg_clients/', reg_clients, name='api_unknow_clients'),
    path('clients_online_count/',
         clients_online_count,
         name='api_clients_online_count'),
]
