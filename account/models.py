from django.db import models
from django.contrib.auth.models import AbstractUser
import pprint
# Create your models here.

class User(AbstractUser):
    is_worker       = models.BooleanField('worker status', default=False)
    is_costumer     = models.BooleanField('costumer status', default=False)

class Degree(models.Model):
    name            = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Position(models.Model):
    name            = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Gender(models.Model):
    name            = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class WorkerManager(models.Manager):
    def is_doctor(self):
        return super(WorkerManager, self).get_queryset().filter(position__name ="Сувилагч")

class Worker(models.Model):

    user            = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='worker')
    firstname       = models.CharField(max_length=200)
    lastname        = models.CharField(max_length=200)
    register        = models.CharField(max_length=200)
    gender          = models.ForeignKey(Gender,on_delete=models.SET_NULL, null=True, blank=True)
    age             = models.IntegerField(null=True, blank=True)
    degree          = models.ForeignKey(Degree, on_delete=models.SET_NULL, null=True, blank=True)
    position        = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.firstname

    def is_doctor(self):
        return self.position.name == "Эмч"
    def is_nurse(self):
        rsp = Worker.objects.filter(position = "Сувилагч")
        return rsp
class Costumer(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='costumer')
    firstname       = models.CharField(max_length=200)
    lastname        = models.CharField(max_length=200)
    register        = models.CharField(max_length=200)
    gender          = models.ForeignKey(Gender,on_delete=models.SET_NULL, null=True, blank=True)
    age             = models.IntegerField(null=True, blank=True)
    description     = models.CharField(max_length=200)

    def __str__(self):
        return self.firstname
