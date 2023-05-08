from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.models import Group

def user_profile(sender, instance, created,**kwargs):
     if created:
        group = Group.objects.get(name='users')
        instance.groups.add(group)
        
        Profile.objects.create(
            user=instance,
            summary=instance.username,
        )

post_save.connect(user_profile, sender=User)