from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Room
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_room(sender, instance, created, **kwargs):
    if created:
        name = instance.username
        slug = slugify(name)
        room = Room.objects.create(name=name, slug=slug)
