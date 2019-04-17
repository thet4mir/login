from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    USER_TYPE_CHOICES = (
      (1, 'doctor'),
      (2, 'nurse'),
      (3, 'costumer'),
      )

    user_type       = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, blank=True)
    is_worker       = models.BooleanField('student status', default=False)
    is_costumer     = models.BooleanField('teacher status', default=False)

class Degree(models.Model):
    name            = models.CharField(max_length=200)
    date            = models.DateField(null=True, blank=True)

class Position(models.Model):
    name            = models.CharField(max_length=200)

class Worker(models.Model):
    GENDER = (
      (1, 'Эр'),
      (2, 'Эм'),
      (3, 'Бусад'),
      )
    user            = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='worker')
    firstname       = models.CharField(max_length=200)
    lastname        = models.CharField(max_length=200)
    register        = models.CharField(max_length=200)
    gender          = models.PositiveSmallIntegerField(choices=GENDER)
    age             = models.IntegerField()
    degree          = models.ForeignKey(Degree, on_delete=models.SET_NULL, null=True, blank=True)
    position        = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)

class Costumer(models.Model):
    GENDER = (
      (1, 'Эр'),
      (2, 'Эм'),
      (3, 'Бусад'),
    )
    user            = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='costumer')
    firstname       = models.CharField(max_length=200)
    lastname        = models.CharField(max_length=200)
    register        = models.CharField(max_length=200)
    gender          = models.PositiveSmallIntegerField(choices=GENDER)
    age             = models.IntegerField()
    description     = models.TextField()
