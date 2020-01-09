from django.contrib.auth.models import User

from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Host, RegisteredHost
from .serializers import HostSerializer, RegisteredHostSerializer
from .facade import ControlDhcpServer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class ApiUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ApiUnknow_clients(APIView):
    def get(self, request, format=None):
        return Response(ControlDhcpServer().unknow_cliets)


class ApiRegistered_clients(APIView):
    def get(self, request, format=None):
        return Response(ControlDhcpServer().dhcp_clients)


class ApiCountClientOnline(APIView):
    def get(self, request, format=None):
        return Response(Host.objects.filter(active=True).count())


class ApiClientOnline(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer


class ApiHostsInDhcpServer(viewsets.ModelViewSet):
    queryset = RegisteredHost.objects.all()
    serializer_class = RegisteredHostSerializer
