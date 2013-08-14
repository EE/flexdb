from rest_framework import viewsets
from custom_user.serializers import CustomUserSerializer
from custom_user.models import CustomUser

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
