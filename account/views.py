from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Costumer, User, Worker
from .forms import CostumerForm, WorkerForm
from django.views.generic import CreateView, ListView

# Create your views here.
class WorkerList(ListView):
    model = Worker

class WorkerCreate(CreateView):
    model = User
    form_class = WorkerForm
    template_name = 'account/worker_create.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('account:worker-list')

class CostumerList(ListView):
    model = Costumer

class CostumerCreate(CreateView):
    model = User
    form_class = CostumerForm
    template_name = 'account/costumer_create.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('account:costumer-list')
