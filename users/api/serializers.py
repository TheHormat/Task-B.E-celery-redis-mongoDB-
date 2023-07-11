from rest_framework import serializers
from users.models import User
from ip_address.models import IPWhitelist


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email"]


class IPWhitelistSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPWhitelist
        fields = ["ip_address"]
