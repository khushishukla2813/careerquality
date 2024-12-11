from django.db import models

class UserProfile(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    type=models.CharField(max_length=128,default='')
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.phone_number} - {self.email}"
