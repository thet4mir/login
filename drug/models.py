from django.db import models
from django.utils import timezone
from account.models import User, Costumer, Worker

# Create your models here.
class Drug_category(models.Model):
    name = models.CharField(max_length=100)

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

class Onosh(models.Model):
    category = models.CharField(max_length=200, null=True, blank=True)
    disc = models.CharField(max_length=400, null=True, blank=True)
    code = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

class Emchilgee(models.Model):
    duration = models.CharField(max_length=50)
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, blank=True)
    costumer = models.ForeignKey(Costumer, on_delete=models.SET_NULL, null=True, blank=True)
    onosh = models.ForeignKey(Onosh, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.worker

class History(models.Model):
    costumer = models.ForeignKey(Costumer, on_delete=models.SET_NULL, null=True, blank=True)
    doctor = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    disc = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.costumer

class Drug_important(models.Model):
    emchilgee = models.ForeignKey(Emchilgee, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.ForeignKey(Drug_detail, on_delete=models.SET_NULL, null=True, blank=True)
    shirheg = models.CharField(max_length=50, null=True, blank=True)
    is_ordered = models.BooleanField('order_status', default=False)

    def __str__(self):
        return self.name

class Drug_order_status(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Drug_order(models.Model):
    date = models.DateField(default=timezone.now)
    number = models.IntegerField()
    recived_date = models.DateField(null=True, blank=True)
    nurse = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, blank=True)
    drug_order_status = models.ForeignKey(Drug_order_status, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.date
