from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from account import views
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from account.models import Worker, User, Costumer
from drug.models import History, Emchilgee
import pprint
class HomePage(LoginRequiredMixin,TemplateView):
    login_url='/account/login/'
    template_name = 'index.html'

@login_required
def Home(request):
    data = {}
    all_work = []
    if request.user.is_worker:
        user = Worker.objects.filter(user=request.user)
        emchilgee = Emchilgee.objects.filter(worker=request.user.worker)
        history = History.objects.filter(doctor=request.user.worker)
    else:
        user = Costumer.objects.filter(user=request.user)

    data['history'] = history
    data['emchilgee'] = emchilgee
    data['user'] = user
    template_name = 'index.html'
    return render(request, template_name, data)
