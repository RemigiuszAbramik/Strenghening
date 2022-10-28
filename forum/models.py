from django.db import models
from django.conf import settings



class Post(models.Model):
    name = models.CharField(max_length=30)
    context = models.TextField(max_length=1000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.name
