from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):

        """ czy tu nie brakuje:
        if request.user.is_superuser:
            return True
            ? """

        if request.method == "DELETE":
            return False

        return True
