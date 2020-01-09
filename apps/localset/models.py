# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from macaddress.fields import MACAddressField
from django.contrib import admin


class Host(models.Model):
    ''' Модель содержащая хосты встречающиеся в сети '''
    ip = models.GenericIPAddressField('IP address', db_index=True)
    mac = MACAddressField(null=True, blank=True)
    vendor = models.CharField('Производитель', max_length=255,
                              null=True, blank=True)
    active = models.BooleanField('Active host', default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {} {}'.format(self.ip, self.mac, self.vendor)

    class Meta:
        ordering = ["ip"]


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = (
        'ip', 'mac', 'vendor', 'active',
        'creation_date', 'update_date',
    )
    search_fields = ('ip', 'mac', 'vendor')
    list_filter = (
        'ip', 'mac', 'vendor', 'active',
        'creation_date', 'update_date',
    )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


class RegisteredHost(models.Model):
    ''' Модель содержащая хосты зарегистрированные в конфиге DHCP сервера '''
    ip = models.GenericIPAddressField('IP address', db_index=True)
    mac = MACAddressField(null=True, blank=True)
    hostname = models.CharField('Host name', max_length=255,
                                null=True, blank=True)
    subnet = models.GenericIPAddressField('Subnet mask', null=True, blank=True)
    routes = models.GenericIPAddressField('Routes', null=True, blank=True)
    dns = models.GenericIPAddressField('DNS', null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ip} {self.hostname}'

    def dt_row_id(self):
        return self.id

    class Meta:
        ordering = ["ip"]


@admin.register(RegisteredHost)
class RegisteredHostAdmin(admin.ModelAdmin):
    list_display = ('ip', 'mac', 'creation_date',)
    search_fields = ('ip', 'mac',)
    list_filter = ('ip', 'mac',)
