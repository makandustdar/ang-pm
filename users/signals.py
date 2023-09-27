from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile_for_new_users(sender, instance, created, **kwargs):
    # pass
    if created:
        Profile.objects.create(user=instance)
