from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.BigIntegerField()
    access_token = models.CharField(max_length=200)

    def __str__(self):
        return self.uid
