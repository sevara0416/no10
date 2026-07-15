from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100, blank=False, null=False)
    price=models.PositiveIntegerField(blank=False, default=0)
    descriptions=models.TextField()
    created_at=models.TimeField(auto_now_add=True)
    created_date=models.DateField(auto_now_add=True)
    updated_at=models.TimeField(auto_now=True)

    def __str__(self):
        return self.name