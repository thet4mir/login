from django import forms
from .models import User, Worker, Costumer, Gender,Position
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
import pprint

class WorkerForm(UserCreationForm):
    firstname   = forms.CharField(max_length=200)
    lastname    = forms.CharField(max_length=200)
    register    = forms.CharField(max_length=200)
    gender      = forms.ModelChoiceField(queryset=Gender.objects.all())
    age         = forms.IntegerField()
    position    = forms.ModelChoiceField(queryset=Position.objects.all())

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)

        user.is_worker = True
        pprint.pprint(user.is_worker)
        user.save()
        worker = Worker.objects.create(user=user)

        worker.firstname = self.cleaned_data.get('firstname')
        worker.lastname = self.cleaned_data.get('lastname')
        worker.register = self.cleaned_data.get('register')
        worker.gender = self.cleaned_data.get('gender')
        worker.position = self.cleaned_data.get('position')
        worker.age = self.cleaned_data.get('age')
        worker.save()
        return user

class CostumerForm(UserCreationForm):
    firstname       = forms.CharField(max_length=200)
    lastname        = forms.CharField(max_length=200)
    register        = forms.CharField(max_length=200)
    gender          = forms.ModelChoiceField(queryset=Gender.objects.all())
    age             = forms.IntegerField()
    description     = forms.CharField(max_length=200)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)

        user.is_costumer = True
        pprint.pprint(user.is_costumer)
        user.save()
        costumer = Costumer.objects.create(user=user)

        costumer.firstname = self.cleaned_data.get('firstname')
        costumer.lastname = self.cleaned_data.get('lastname')
        costumer.register = self.cleaned_data.get('register')
        costumer.gender = self.cleaned_data.get('gender')
        costumer.age = self.cleaned_data.get('age')
        costumer.description = self.cleaned_data.get('description')
        pprint.pprint(self.cleaned_data.get('description'))
        costumer.save()
        return user
