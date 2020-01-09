import re

from .models import RegisteredHost
from .services.parser_dhcp_conf import ParserDhcpConf
from .services.connect_server import ssh_conect, ssh_conect_dhcp
from apps.services_functions.string_functions import get_val_if_key

''' Фасад реализующий управление DHCP сервером.
    ControlDhcpServer - класс управляющий DHCP сервером

    Для ускорения работы все значения конфигурации DHCP сервера
    хранятся в базе данных и управляются классом прослойкой
    SettingsDhcpInBase - класс прослока

'''


class ControlDhcpServer():
    ''' Класс управляющий DHCP сервером
    '''
    _active_server = None
    _registers_mac = set()  # список зарегистрированных mac адресов;
    _dhcp_clients = []  # список зарегистрированных соответсвий ip-mac
    _unknow_cliets = set()  # список не зарегистрированных  mac адресов;

    def __init__(self, host=None, user=None, passwd=None):
        if not host or not user or not passwd:
            self._active_server = ssh_conect_dhcp()
        else:
            self._active_server = ssh_conect(host, user, passwd)

    def leases(self):
        ''' Производится разбор лога DHCP сервера
            на данный момент времени
            и заполняются:
            _registers_mac - список зарегистрированных mac адресов;
            _dhcp_clients - список зарегистрированных соответсвий ip-mac;
            unknow_cliets - список не зарегистрированных  mac адресов;
        '''
        stdin, stdout, stderr = self._active_server.exec_command(
            "cat /var/log/dhcpd.log")
        log = stdout.read().decode('utf-8')
        for line in log.splitlines():
            self.find_unknow_client_to_log(line)
            self.find_pack_ip_client_to_log(line)

    def clear_log(self):
        self._active_server.exec_command("cat /dev/null > /var/log/dhcpd.log")

    def find_unknow_client_to_log(self, line):
        ''' Проверка на наличие в переданной сторке line
            наличие записи "DHCPDISCOVER.*unknown"
            Если найдена, то добавляем найденным mac адресов в
            список не зарегистрированных mac адресов
        '''
        tmp_r = re.findall(r'DHCPDISCOVER.*unknown', line)
        if tmp_r:
            self._unknow_cliets.update(re.findall(
                r'(?<!:)\b(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b(?!:)', line))

    def find_pack_ip_client_to_log(self, line):
        ''' Проверка на наличие в переданной сторке line
            наличие записи "DHCPACK"
            Если найдена, то добавляем найденным mac адресов в
            список зарегистрированных mac адресов и
            список зарегистрированных соответсвий ip-mac
        '''
        tmp_r = re.findall(r'DHCPACK', line)
        if tmp_r:
            mac = re.findall(
                r'(?<!:)\b(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b(?!:)', line)
            ip = re.findall(
                r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
            if mac and not mac[0] in self._registers_mac:
                self._registers_mac.update(mac)
                self._dhcp_clients.append(
                    {'mac': mac[0] if mac else '',
                     'ip': ip[0] if ip else ''})

    @property
    def hosts_in_dhcp_server(self):
        return ParserDhcpConf().execute()

    @property
    def dhcp_clients(self):
        self.leases()
        return self._dhcp_clients

    @property
    def registers_mac(self):
        self.leases()
        return self._registers_mac

    @property
    def unknow_cliets(self):
        self.leases()
        return self._unknow_cliets


class SettingsDhcpInBase():
    ''' класс прослока между значениями хранящимися
        в конфигурациях DHCP сервера и значениями в базе данных.

    '''
    model = RegisteredHost

    def __init__(self, host=None, user=None, passwd=None):
        self.control_dhcp_derver = ControlDhcpServer(host, user, passwd)

    def dhcp_clients_from_config_to_base(self):
        dhcp_clients = self.control_dhcp_derver.hosts_in_dhcp_server
        for dhcp_client in dhcp_clients:
            # создается словарь обновляемых полей
            defaults = dict(zip(
                ['hostname', 'routes', 'subnet', 'dns'],
                map(lambda x: get_val_if_key(dhcp_client, x),
                    [ParserDhcpConf.TAG_HOST_NAME,
                     ParserDhcpConf.TAG_ROUTER,
                     ParserDhcpConf.TAG_SUBNET,
                     ParserDhcpConf.TAG_DNS])))
            self.model.objects.update_or_create(
                mac=dhcp_client[ParserDhcpConf.TAG_MAC],
                ip=dhcp_client[ParserDhcpConf.TAG_ADDR],
                defaults=defaults)
