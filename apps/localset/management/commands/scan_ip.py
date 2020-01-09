from django.core.management.base import BaseCommand
from apps.localset.services.local_service import scan_ip


class Command(BaseCommand):
    help = "changes mailing list status"

    def handle(self, *args, **options):
        scan_ip()
