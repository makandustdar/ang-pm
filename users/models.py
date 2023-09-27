from django.db import models
from django.conf import settings
from base.models import Department
from .managers import MechanicalManager


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mobileNumber = models.CharField(max_length=11, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    objects = models.Manager()
    mechanical_users = MechanicalManager()

    def __str__(self):
        if self.user.first_name:
            return f'{self.user.first_name} {self.user.last_name}'
        else:
            return 'مدیریت'
