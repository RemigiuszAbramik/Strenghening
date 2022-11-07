from django.db import models
from django.conf import settings

class Diet(models.Model):
    name = models.CharField(max_length=30)
    context = models.TextField(max_length=1000)
    image = models.ImageField(default="diet_pics/default.png", upload_to='diet_pics')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id) + ' - ' + self.name
