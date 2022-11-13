from django.db import models
from django.conf import settings
from django.urls import reverse
from login.models import Profile


class Post(models.Model):
    name = models.CharField(max_length=100)
    context = models.TextField(max_length=1000)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('forum:index')


class Comment(models.Model):
    context = models.TextField(max_length=1000)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", null=True)

    def __str__(self):
        return "| " + str(self.author) + " | " + " - " + " | " + str(self.post) + " | "
