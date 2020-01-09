import re
from .connect_server import ssh_conect_dhcp


class ParserDhcpConf(object):
    ''' Класс преобразование конфигурационного файла настройки хостов
        DHCP сервера в список с словарями
    '''

    # маркеры начала, конца записи хоста
    # и опиций хоста в конфиге dhcp пользователей
    (TAG_START_ITEM, TAG_END_ITEM,
     TAG_MAC, TAG_ADDR, TAG_HOST_NAME,
     TAG_SUBNET, TAG_ROUTER, TAG_DNS) = (
        '^host .*{', '}',
        'hardware ethernet', 'fixed-address', 'ddns-hostname',
        'subnet-mask', 'routers', 'domain-name-servers',
    )

    # маркеры и регулярыне значения опиций хоста в конфиге dhcp пользователей
    tags = {
        TAG_START_ITEM: TAG_START_ITEM,
        TAG_END_ITEM: TAG_END_ITEM,
        TAG_MAC:
            r'((?<!:)\b(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b(?!:))',
        TAG_ADDR:
            r'fixed-address (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3});',
        TAG_HOST_NAME: r'ddns-hostname (.*);',
        TAG_SUBNET: r'subnet-mask (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3});',
        TAG_ROUTER: r'routers (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3});',
        TAG_DNS:
            r'domain-name-servers (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3});',
    }

    hosts = []

    def get_value(self, tag, line, dict_item):
        '''Фуннкция возвращает переданный словарь(dict_item)
            вставив в него значение со сотроки(line),
            полученое при помощи переданого маркера(tag).
        '''
        result = re.search(self.tags[tag], line)
        if result and result.groups():
            dict_item[tag] = result.group(1)
            return dict_item

    def what_active_tag_in_line(self, line):
        ''' Функция возвращает найденный маркер в текущей строке'''
        for key, tag in self.tags.items():
            pattern = re.compile(f'{key}')
            result = pattern.search(line)
            if result:
                return key

    def execute(self):
        ssh = ssh_conect_dhcp()
        stdin, stdout, stderr = ssh.exec_command("cat /etc/dhcp/inet.users")
        log = stdout.read().decode('utf-8')
        for line in log.splitlines():
            active_tag = self.what_active_tag_in_line(line)
            if not active_tag:
                continue  # при отсутствии необходимого маркера переходим далее
            if active_tag == self.TAG_START_ITEM:
                new_item = {}  # начало нового хоста в конфиге -> новый словарь
                continue
            elif active_tag == self.TAG_END_ITEM and new_item:
                self.hosts.append(new_item)  # конец опции по хосту в конфиге
                continue  # заносим словарь в список
            self.get_value(active_tag, line, new_item)
        return self.hosts
