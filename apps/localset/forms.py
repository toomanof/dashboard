from django import forms

from .models import RegisteredHost, Host


class OnLineHostForm(forms.ModelForm):

    class Meta:
        model = Host
        fields = ('ip', 'mac', 'vendor', 'active')

class RegisteredHostForm(forms.ModelForm):

    class Meta:
        model = RegisteredHost
        fields = ('ip', 'mac', 'hostname', 'subnet', 'routes', 'dns')
