from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    groups = models.ManyToManyField(
        Group,
        related_name="%(app_label)s_%(class)s_related",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="%(app_label)s_%(class)s_related",
        blank=True,
    )

    def __str__(self):
        return self.email

    @property
    def group(self):
        groups = self.groups.all()
        return [group.name for group in groups if groups]


class Roles(models.Model):
    name = models.CharField(max_length=20, default="")


class Pages(models.Model):
    name = models.CharField(max_length=20, default="")


class Endpoints(models.Model):
    route = models.CharField(max_length=20, default="")


class CustomUserRoles(models.Model):
    role_id = models.ForeignKey(Roles, on_delete=models.PROTECT)
    custom_user_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT)


class RolesEndpoints(models.Model):
    name = models.CharField(max_length=20, default="")
    role_id = models.ForeignKey(Roles, on_delete=models.PROTECT)
    endpoints_id = models.ForeignKey(Endpoints, on_delete=models.PROTECT)


class RolesPages(models.Model):
    name = models.CharField(max_length=20, default="")
    role_id = models.ForeignKey(Roles, on_delete=models.PROTECT)
    page_id = models.ForeignKey(Pages, on_delete=models.PROTECT)
