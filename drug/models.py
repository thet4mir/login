from django.db import models
from django.utils import timezone
from account.models import User, Costumer, Worker
from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, timedelta
import datetime
import pprint

# Create your models here.
class Drug_category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Drug_detail(models.Model):
    name            = models.CharField(max_length=100)
    size            = models.CharField(max_length=50)
    nairlaga        = models.CharField(max_length=100)
    intro           = models.CharField(max_length=100)
    other_side      = models.CharField(max_length=100)
    zaavar          = models.CharField(max_length=100)
    age             = models.IntegerField()
    duration        = models.CharField(max_length=50)
    date            = models.DateField(default=timezone.now)
    factory         = models.CharField(max_length=100)
    price           = models.IntegerField()
    drug_catedory   = models.ForeignKey(Drug_category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Onosh(models.Model):
    category    = models.CharField(max_length=200, null=True, blank=True)
    disc        = models.CharField(max_length=400, null=True, blank=True)
    code        = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.disc

class Emchilgee(models.Model):
    start_date      = models.DateField(default=timezone.now)
    end_date        = models.DateField(default=timezone.now)
    worker          = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, blank=True)
    costumer        = models.ForeignKey(Costumer, on_delete=models.SET_NULL, null=True, blank=True)
    onosh           = models.ForeignKey(Onosh, on_delete=models.SET_NULL, null=True, blank=True)
    created_date    = models.DateField(default=timezone.now)

    def is_started(self):
        return self.start_date <= date.today()

    def is_done(self):
        return self.end_date < date.today()

    def has_review(self):
         rsp = get_object_or_404(Doctor_review, emchilgee = self.id)
         return rsp
    def count_days(self):
        result = self.end_date + timedelta(days=1) - self.start_date
        return int(result.days)

class Days_of_emchilgee(models.Model):
    emchilgee               = models.ForeignKey(Emchilgee, on_delete=models.CASCADE, default=1)
    day                     = models.DateField(default=timezone.now)
    is_done                 = models.BooleanField(default=False)

    def __str__(self):
        return str(self.emchilgee.id)

class Emchilgee_list(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class History(models.Model):
    costumer        = models.ForeignKey(Costumer, on_delete=models.SET_NULL, null=True, blank=True)
    doctor          = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, blank=True)
    created_date    = models.DateField(default=timezone.now)
    disc            = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.costumer

class Drug_important(models.Model):
    emchilgee               = models.ForeignKey(Emchilgee, on_delete=models.CASCADE, default=1)
    emchilgee_list          = models.ForeignKey(Emchilgee_list, on_delete=models.SET_NULL, null=True, blank=True)
    name                    = models.ForeignKey(Drug_detail, on_delete=models.SET_NULL, null=True, blank=True)
    shirheg                 = models.IntegerField(default=0)
    is_ordered              = models.BooleanField('ordered_status', default=False)

    def __str__(self):
        return self.name.name

class Drug_order_status(models.Model):
    name    = models.CharField(max_length=100)
    about   = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Drug_order(models.Model):
    name            = models.ForeignKey(Drug_detail, on_delete=models.SET_NULL, null=True, blank=True)
    number          = models.IntegerField(default=0)
    ordered_date    = models.DateField(default=timezone.now)
    recived_date    = models.DateField(null=True, blank=True)
    nurse           = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.date
class Doctor_review(models.Model):
    emchilgee       = models.IntegerField(default=0)
    doctor          = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, blank=True)
    review          = models.IntegerField(default=1)

class Costumer_review(models.Model):
    emchilgee       = models.IntegerField(default=0)
    costumer        = models.ForeignKey(Costumer, on_delete=models.SET_NULL, null=True, blank=True)
    review          = models.IntegerField(default=1)
