from django.urls import path
from .views import (
    UserDetailUpdateAPIView,
    UserListCreateAPIView,
    IPWhitelistAPIView
)

urlpatterns = [
    path("user/<int:id>/", UserDetailUpdateAPIView.as_view(), name="user-detail-update"),
    path("user/", UserListCreateAPIView.as_view(), name="user-list-create"),
    path('ipwhitelist/', IPWhitelistAPIView.as_view(), name='ipwhitelist'),
]
