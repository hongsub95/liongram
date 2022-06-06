from rest_framework import serializers
from rest_framework.authtoken.models import Token
from users import models as users_models

class AccountBaseSerailizers(serializers.ModelSerializer):
    class Meta:
        model = users_models.User
        field = "__all__"

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = "__all__"