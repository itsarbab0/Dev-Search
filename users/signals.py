from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.conf import settings

#@receiver(post_save, sender= Profile)
def createUpdate(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name, 
        )
        
        
        subject = 'Welcome to DevSearch'
        message = 'We are glad you are here!'
    
        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [profile.email],
                fail_silently=False,
            )
        except:
            print('Email failed to send...')

def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete() 
    
post_save.connect(createUpdate, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender= Profile)