from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(default="profile_pics/default.png", upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

