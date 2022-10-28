from django.db import models


class Training(models.Model):
    name = models.CharField(max_length=30)
    context = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.id) + ' - ' + self.name
