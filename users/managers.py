from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class MechanicalManager(models.Manager):
    def get_queryset(self):
        return super(MechanicalManager, self).get_queryset().filter(user__groups__name__in=['کاربر فنی'])
