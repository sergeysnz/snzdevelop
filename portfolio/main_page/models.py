from django.db import models

# Create your models here.


class CallBackMail(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    objects = models.Manager()


class CallBackPhone(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
