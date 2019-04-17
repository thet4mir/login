from django import forms
from .models import User, Worker, Costumer

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ('register', 'gender', 'age', 'degree', 'position')

class CostumerForm(forms.ModelForm):
    class Meta:
        model = Costumer
        fields = ('register', 'gender', 'age', 'description')
