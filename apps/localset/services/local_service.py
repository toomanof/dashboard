''' Функции сервиса сети
'''
import nmap

from ..models import Host


def scan_ip():
    '''Сканирование сети'''
    active_ip()


def active_ip():
    Host.objects.all().update(active=False)
    nm = nmap.PortScanner()
    active_scan = nm.scan(hosts='172.16.0.0/22', arguments='-sP -T4')
    for ip, value in active_scan['scan'].items():
        if 'mac' in value['addresses']:
            mac = value['addresses']['mac']
            vendor = value['vendor'][mac] if mac in value['vendor'] else ''
            Host.objects.update_or_create(
                ip=ip,
                defaults={'mac': mac,
                          'vendor': vendor,
                          'active': True}
            )
