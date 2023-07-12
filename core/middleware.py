# # core/middleware.py

# from ip_address.models import IPWhitelist
# from django.http import HttpResponseForbidden


# class IPWhitelistMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         ip = request.META.get("HTTP_X_FORWARDED_FOR") or request.META.get("REMOTE_ADDR")

#         if not IPWhitelist.objects.filter(ip_address=ip).exists():
#             return HttpResponseForbidden("IP not whitelisted")

#         return self.get_response(request)
