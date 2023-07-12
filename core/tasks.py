from celery import shared_task
from django.utils import timezone
from ip_address.models import IPWhitelist

@shared_task
def delete_expired_ips():
    expiration_time = timezone.now() - timezone.timedelta(minutes=5)
    IPWhitelist.objects.filter(created_at__lt=expiration_time).delete()
