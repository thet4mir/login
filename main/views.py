from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from account import views
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from account.models import Worker, User, Costumer

class HomePage(LoginRequiredMixin,TemplateView):
    login_url='/account/login/'
    template_name = 'index.html'

@login_required
def Home(request):
    data = {}
    if request.user.is_worker:
        user = Worker.objects.filter(user=request.user)
    else:
        user = Costumer.objects.all(user=request.user)

    data['user'] = user
    template_name = 'index.html'
    return render(request, template_name, data)
