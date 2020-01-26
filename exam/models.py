from django.db import models

# Create your models here.

class Questions(models.Model):
    id        = models.AutoField(primary_key=True)
    questpack = models.CharField(max_length=500)
    A    = models.CharField(max_length=500)
    B    = models.CharField(max_length=500)
    C    = models.CharField(max_length=500)
    D    = models.CharField(max_length=500)
    truequest = models.CharField(max_length=50, blank=True, null=True)


class Chosen(models.Model):
    id        = models.AutoField(primary_key=True)
    questpack = models.CharField(max_length=500)
    A    = models.CharField(max_length=500)
    B    = models.CharField(max_length=500)
    C    = models.CharField(max_length=500)
    D    = models.CharField(max_length=500)

    AB   = models.BooleanField(default=False, blank=True, null=True)
    BB   = models.BooleanField(default=False, blank=True, null=True)
    CB   = models.BooleanField(default=False, blank=True, null=True)
    DB   = models.BooleanField(default=False, blank=True, null=True)

    none = models.BooleanField(default=False, blank=True, null=True)
    truequest = models.CharField(max_length=50, blank=True, null=True)


class Users(models.Model):
    password = models.CharField(max_length=250)
    username = models.CharField(max_length=50, unique=True)
    email    = models.EmailField(max_length=90, unique=True)

    class Meta:
        ordering = ["username"]