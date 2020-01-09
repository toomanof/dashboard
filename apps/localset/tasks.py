from .facade import ControlDhcpServer
from .services.local_service import scan_ip
from celery.decorators import periodic_task
from celery.task.schedules import crontab


@periodic_task(run_every=crontab(minute='*/5'))
def scan_network():
    scan_ip()


@periodic_task(run_every=crontab(minute=0, hour=0))
def clear_dhcp_log():
    ControlDhcpServer().clear_log()
