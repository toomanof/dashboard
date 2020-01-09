from django.core.management.base import BaseCommand

from apps.localset.services.export_sqlite import export


class Command(BaseCommand):
    help = "changes mailing list status"

    def handle(self, *args, **options):
        export()
