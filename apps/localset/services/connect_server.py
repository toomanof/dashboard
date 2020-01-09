import paramiko
from django.conf import settings


def ssh_conect(server, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server, username=username, password=password)
    return ssh


def ssh_conect_dhcp():
    return ssh_conect(
        settings.DHCP_SERVER, settings.DHCP_USER, settings.DHCP_PASSWORD)


def ssh_conect_firewall():
    return ssh_conect(
        settings.FW_SERVER, settings.FW_USER, settings.FW_PASSWORD)
