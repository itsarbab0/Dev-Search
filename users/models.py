from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db import models
# Create your models here.
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank= True )
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=500, null=True)
    username = models.CharField(max_length=200, null=True)
    location= models.CharField(max_length=200, null=True)
    short_intro = models.CharField(max_length=200, null=True, blank= True )
    profile_image = models.ImageField( null=True, blank= True , upload_to='profiles' , default="profiles/pro.png")
    social_github = models.CharField(max_length=200, null=True, blank= True )
    social_twitter = models.CharField(max_length=200, null=True, blank= True )
    social_linkedin = models.CharField(max_length=200, null=True, blank= True )
    social_stackoverflow = models.CharField(max_length=200, null=True, blank= True )
    description = models.TextField(blank=True)
    bio = models.TextField(max_length=500,blank=True, null=True),
    social_website = models.CharField(max_length=200, null=True, blank= True )
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                        primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.username)
    
    
class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank= True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank= True)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default=uuid.uuid4, unique= True, primary_key= True, editable=False)
    
    def __str__(self):
        return self.name
    

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']


