from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20, null=True)
    lastname = models.CharField(max_length=20, null=True)
    phone = models.PositiveBigIntegerField(null=True)
    bio = models.TextField(null=True)
    country = models.CharField(max_length=20, null=True)


    def get_object(self):
        return self.request.user