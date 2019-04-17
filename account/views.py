from django.shortcuts import render
from .models import Costumer, User, Worker
from .forms import CostumerForm, WorkerForm, UserForm
# Create your views here.

def WorkerCreate(request):

    user_form = UserForm(request.POST or None, prefix='UF')
    worker_form = WorkerForm(request.POST or None, prefix='PF')

    if request.method == "POST":
	       if user_form.is_valid() and worker_form.is_valid():

                user = user_form.save(commit=False)
                user.save()

                user.worker.register = worker_form.cleaned_data.get('register')
                user.worker.register = worker_form.cleaned_data.get('gender')
                user.worker.register = worker_form.cleaned_data.get('age')
                user.worker.register = worker_form.cleaned_data.get('degree')
                user.worker.register = worker_form.cleaned_data.get('position')
                user.worker.save()

    return render(request, 'account/worker_create.html', {'user_form': user_form, 'worker_form': worker_form})
