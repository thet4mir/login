from django.views.generic import TemplateView
from django.shortcuts import redirect
from account import views
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePage(LoginRequiredMixin,TemplateView):
    login_url='/account/login/'
    template_name = 'index.html'
