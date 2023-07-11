from django.urls import path
from .views import (
    UserDetailAPIView,
    UserListCreateAPIView,
    UserUpdateAPIView,
    IPWhitelistAPIView
)

urlpatterns = [
    path("user/<int:id>/", UserDetailAPIView.as_view(), name="user-detail"),
    path("user/", UserListCreateAPIView.as_view(), name="user-list-create"),
    path("user/<int:id>/", UserUpdateAPIView.as_view(), name="user-update"),
    path('ipwhitelist/', IPWhitelistAPIView.as_view(), name='ipwhitelist'),
]
