from rest_framework import permissions
from ip_address.models import IPWhitelist


class IPWhitelistPermission(permissions.BasePermission):
    message = "Your IP address is blocked."

    def has_permission(self, request, view):
        whitelisted_ips = IPWhitelist.objects.values_list("ip_address", flat=True)
        client_ip = request.META.get("REMOTE_ADDR")
        return client_ip in whitelisted_ips
