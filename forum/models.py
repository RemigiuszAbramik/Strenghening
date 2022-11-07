from django.db import models
from django.conf import settings
from django.urls import reverse


class Post(models.Model):
    name = models.CharField(max_length=100)
    context = models.TextField(max_length=1000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})