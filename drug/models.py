from django.db import models
from django.utils import timezone
from account.models import User

# Create your models here.
class Drug_category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Emchilgee(models.Model):
    duration = models.CharField(max_length=50)
    costumer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.duration

class History(models.Model):
    costumer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    disc = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.disc

class Onosh(models.Model):
    costumer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    disc = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Drug_important(models.Model):
    emchilgee = models.ForeignKey(Emchilgee, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True )
    shirheg = models.CharField(max_length=50, null=True, blank=True)
    category = models.ForeignKey(Drug_category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Drug_order_status(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Drug_detail(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    nairlaga = models.CharField(max_length=100)
    intro = models.CharField(max_length=100)
    other_side = models.CharField(max_length=100)
    zaavar = models.CharField(max_length=100)
    age = models.IntegerField()
    duration = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    factory = models.CharField(max_length=100)
    price = models.IntegerField()
    drug_catedory = models.ForeignKey(Drug_category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Drug_order(models.Model):
    date = models.DateField(default=timezone.now)
    number = models.IntegerField()
    recived_date = models.DateField(default=timezone.now)
    about = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    drug_order_status = models.ForeignKey(Drug_order_status, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.date
