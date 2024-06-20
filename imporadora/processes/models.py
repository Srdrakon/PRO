# processes/models.py
# processes/models.py
# processes/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"