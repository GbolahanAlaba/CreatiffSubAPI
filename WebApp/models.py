from django.db import models

class Subscriptions(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=280)

    def __str__(self):
        return self.Name + ' ' + self.Email


# Create your models here.
