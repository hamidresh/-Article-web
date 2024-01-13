# models.py

from django.db import models
from authors.models import Profile_authors
from django.dispatch import receiver
from django.db.models.signals import post_save


class Essay(models.Model):
    author = models.ForeignKey(Profile_authors , null=True
                              ,on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title if self.title else f"Untitled Essay {self.pk}"

@receiver(post_save, sender=Essay)
def update_title_variable(sender, instance, **kwargs):
    if instance.title is None and instance.pk:
        instance.title = f"Article {instance.pk}"
        instance.save()

class Comment(models.Model):
    essay = models.ForeignKey(Essay, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:50]