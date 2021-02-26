from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudentUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20,null=True)
    mobile = models.IntegerField(null=True)
    image = models.FileField(null=True)
    type = models.CharField(max_length=15,null=True)

    def __str__(self):
        return self.user.username

class RecruiterUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20,null=True)
    mobile = models.IntegerField(null=False)
    company = models.CharField(max_length=40, null=True)
    image = models.FileField(null=False)
    type = models.CharField(max_length=15,null=True)
    status = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.user.username