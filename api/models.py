from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.utils.text import slugify

class CustomUser(AbstractUser):
    name=models.CharField(max_length=100, blank=False, null=False)
    age=models.PositiveIntegerField(default=18)
    phone_number=models.CharField(max_length=50, blank=False)

class Post(models.Model):
    title=models.CharField(max_length=100)
    comment=models.TextField()
    likes=models.IntegerField(default=0)
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="post")
    # tag=models.
    created_at=models.DateTimeField(auto_now_add=True)
    created_date=models.DateField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
