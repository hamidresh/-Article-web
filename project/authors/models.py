from django.db import models
import uuid
from django.contrib.auth.models import User

from django.db.models.signals import post_save , post_delete

from django.core.mail import send_mail
from django.conf import settings
# Create your models here.

class Profile_authors(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    username = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=500,blank=True,null=True)
    bio =  models.TextField(max_length=100,blank=True,null=True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True,primary_key=True,editable=False)
    confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

def profilecreat (sender , instance , created , **kwargs):
    if created :
        user = instance
        authors = Profile_authors.objects.create(
            user = user ,
            email = user.email ,
            username = user.username , 

        )
        subject = u""
        message = u""
        send_mail (
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [authors.email],
            fail_silently=False,
                )


def authorsdelet (sender , instance , **kwargs):
    user = instance.user
    user.delete()


post_save.connect(profilecreat,sender=User)