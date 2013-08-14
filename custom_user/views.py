from rest_framework import viewsets
from custom_user.serializers import CustomUserSerializer
from custom_user.models import CustomUser


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    model = CustomUser

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(id=user.id)
