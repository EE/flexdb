from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from flexdb.utils import get_config, PermissionExeption


class CustomUserManager(BaseUserManager):
    def create_user(self, username=None, email=None, password=None):
        if not username:
            raise ValueError('The given username must be set')

        user = self.model(username=username, email=email,
                          is_staff=False, is_active=True, is_superuser=False)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField("user name", max_length=127, unique=True)
    first_name = models.CharField("first name", max_length=63, blank=True)
    last_name = models.CharField("last name", max_length=63, blank=True)
    email = models.EmailField("email", blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        full_name = "{} {}".format(self.first_name, self.last_name)
        return full_name.strip()

    def __unicode__(self):
        return self.username

    def has_permisson(self, app_name, permission_name):
        perm = UsersPermissions.objects.filter(user=self, app_name=app_name, permission_name=permission_name).count()
        if perm > 0:
            return True
        return False

    def add_permission(self, app_name, permission_name):
        config = get_config(app_name)
        if not config.has_permission(permission_name):
            raise PermissionExeption(app_name, permission_name)
        perm = UsersPermissions(user=self, app_name=app_name, permission_name=permission_name)
        perm.save()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()


class UsersPermissions(models.Model):
    user = models.ForeignKey(CustomUser)
    app_name = models.CharField(max_length=127)
    permission_name = models.CharField(max_length=127)

    def __unicode__(self):
        return "{}, {}, {}".format(self.user.username, self.app_name, self.permission_name)
