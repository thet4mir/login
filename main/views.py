from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from account import views
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from account.models import Worker, User, Costumer
from drug.models import History, Emchilgee, Doctor_review, Costumer_review
import pprint
class HomePage(LoginRequiredMixin,TemplateView):
    login_url='/account/login/'
    template_name = 'index.html'

@login_required
def Home(request):
    data = {}
    all_work = []
    pprint.pprint(request.user)
    pprint.pprint(request.user.worker)
    if request.user.is_worker:
        pprint.pprint('worker')
        if request.user.worker.is_doctor():
            pprint.pprint('doctor')
            user = Worker.objects.filter(user=request.user)
            emchilgee = Emchilgee.objects.all()
            #history = History.objects.filter(doctor = request.user.worker)
            #data['doctor_review'] =Doctor_review.objects.all()
            #data['history'] = history
            #data['emchilgee'] = emchilgee
        else:
            pprint.pprint('nurse')
            user = Worker.objects.filter(user=request.user)
            pprint.pprint(request.user)
            emchilgee = Emchilgee.objects.filter(worker = request.user.worker)
            pprint.pprint('****')
            #emchilgee = Emchilgee.objects.all()
            #history = History.objects.all()
            #data['doctor_review'] =Doctor_review.objects.all()
            #data['history'] = history
            #data['emchilgee'] = emchilgee
    else:
        user = Costumer.objects.filter(user=request.user)
        #emchilgee = Emchilgee.objects.filter(costumer=request.user.costumer)
        #history = History.objects.filter(costumer=request.user.costumer)
        #data['history'] = history
        #data['emchilgee'] = emchilgee

    #data['costumer_review'] = Costumer_review.objects.all()
    data['emchilgee'] = emchilgee
    data['user'] = user
    template_name = 'index.html'
    return render(request, template_name, data)
