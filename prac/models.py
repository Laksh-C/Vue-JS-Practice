from django.db import models

# Create your models here.
class practice(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 400)
    price = models.IntegerField()

    def __str__(self):
        return self.title 