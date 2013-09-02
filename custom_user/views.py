from rest_framework import viewsets
from custom_user.serializers import CustomUserSerializer
from custom_user.models import CustomUser
from custom_user.permissions import IsOwner
from django.shortcuts import render
from django.http import HttpResponse


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    model = CustomUser
    permission_classes = (IsOwner,)

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(id=user.id)


def userEditView(request):
    if request.user.is_authenticated():
        data = {}
        data['users'] = CustomUser.objects.all()#only("username", "first_name", "last_name", "email")
        data['edit'] = request.user.has_permission('custom_user', 'edit')
        data['perm'] = request.user.has_permission('custom_user', 'permissions')
        return render(request, 'custom_user/custom_user.html', data)
    return HttpResponse("")
