from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    comment=models.TextField()
    likes=models.IntegerField(default=0)
    author=models.CharField(max_length=100)
    # tag=models.
    created_at=models.TimeField(auto_now_add=True)
    created_date=models.DateField(auto_now_add=True)
    updated_at=models.TimeField(auto_now=True)

    def __str__(self):
        return self.title
    