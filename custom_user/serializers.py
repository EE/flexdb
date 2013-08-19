from rest_framework import serializers
from custom_user.models import CustomUser


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('url', 'username', 'first_name', 'last_name', 'email')
