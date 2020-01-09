from django.core.management.base import BaseCommand

from apps.localset.facade import SettingsDhcpInBase


class Command(BaseCommand):
    help = "changes mailing list status"

    def handle(self, *args, **options):
        SettingsDhcpInBase().dhcp_clients_from_config_to_base()
