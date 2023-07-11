from django.db import models

# Create your models here.
class IPWhitelist(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)

    def __str__(self):
        return self.ip_address
