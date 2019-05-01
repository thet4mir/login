from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError
from datetime import date

from .models import Drug_category, doctor_review, costumer_review, Drug_detail, Drug_order, Drug_order_status, Drug_important, Emchilgee, Onosh, History, Worker, Costumer
from .forms import Drug_detail_create_form, Drug_important_form, Emchilgee_form, OnoshForm, HistoryForm
import pprint

# Create your views here.
def drug_detail(request, template_name='drug/drug_detail.html'):
    data = {}
    drug_detail = Drug_detail.objects.all()
    form = Drug_detail_create_form(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('drug:drug_detail')

    data['drug_detail'] = drug_detail
    data['form'] = form
    return render(request, template_name, data)

def emchilgee_create(request, template_name='drug/emchilgee_create.html'):
    context = {}
    emchilgee = Emchilgee.objects.all()
    drug_important = Drug_important.objects.all()

    Drug_important_formset = modelformset_factory(Drug_important, form=Drug_important_form)

    form = Emchilgee_form(request.POST or None)
    formset1 = Drug_important_formset(request.POST or None, queryset = Drug_important.objects.none(), prefix='drug_important')

    if request.method == "POST":
        if form.is_valid():
            try:
                with transaction.atomic():
                    emchilgee = form.save(commit=False)
                    emchilgee.save()

                    if formset1.is_valid():
                        for drug_important in formset1:
                            data = drug_important.save(commit=False)
                            data.emchilgee = emchilgee
                            data.save()
            except IntegrityError:
                print("Error Encountered")

            return redirect('drug:emchilgee_create')

    context['drug_important'] = drug_important
    context['emchilgee'] = emchilgee
    context['formset1'] = formset1
    context['form'] = form
    return render(request, template_name, context)

def onosh_create(request, template_name='drug/onosh_create.html'):
    context = {}
    OnoshFormset = modelformset_factory(Onosh, form=OnoshForm)

    formset1 = OnoshFormset(request.POST or None, queryset = Onosh.objects.none(), prefix='onosh')

    if request.method == "POST":
        if formset1.is_valid():
            try:
                with transaction.atomic():
                    for onosh in formset1:
                        data = onosh.save(commit=False)
                        data.save()

            except IntegrityError:
                print("Error Encountered")

            return redirect('drug:onosh_list')

    context['formset1'] = formset1
    return render(request, template_name, context)
def onosh_list(request, template_name='drug/onosh_list.html'):

    onosh = Onosh.objects.all()

    data = {}
    data['onosh'] = onosh

    return render(request, template_name, data)

def history_create(request, template_name='drug/history_create.html'):
    context = {}
    HistoryFormset = modelformset_factory(History, form=HistoryForm)

    formset1 = HistoryFormset(request.POST or None, queryset = History.objects.none(), prefix='history')

    if request.method == "POST":
        if formset1.is_valid():
            try:
                with transaction.atomic():
                    for history in formset1:
                        data = history.save(commit=False)
                        data.save()

            except IntegrityError:
                print("Error Encountered")

            return redirect('drug:history_list')

    context['formset1'] = formset1
    return render(request, template_name, context)

def history_list(request, template_name='drug/history_list.html'):

    history = History.objects.all()

    data = {}
    data['history'] = history

    return render(request, template_name, data)


def emchilgee_list(request, template_name='drug/emchilgee_list.html'):
    data = {}
    temp = []
    today = date.today()
    emchilgee = Emchilgee.objects.filter(worker = request.user.worker)
    drug_important = Drug_important.objects.all()
    for item in emchilgee:
        if item.end_date > today:
            temp.append(item)

    emchilgee = temp
    data['drug_important'] = drug_important
    data['emchilgee'] = emchilgee

    return render(request, template_name, data)

def emchilgee_list_done(request, template_name='drug/emchilgee_list_done.html'):
    data = {}
    temp = []
    today = date.today()
    emchilgee = Emchilgee.objects.filter(worker = request.user.worker)
    drug_important = Drug_important.objects.all()
    for item in emchilgee:
        if item.end_date < today:
            temp.append(item)

    emchilgee = temp
    data['drug_important'] = drug_important
    data['emchilgee'] = emchilgee

    return render(request, template_name, data)

def all_emchilgee_list(request, template_name='drug/all_emchilgee_list.html'):
    data = {}
    emchilgee = Emchilgee.objects.all()

    if request.method == "POST":
        if request.POST['emchilgee_id']:
            pprint.pprint(request.POST[id])

    data['emchilgee'] = emchilgee

    return render(request, template_name, data)


def drug_order(request, template_name='drug/drug_order.html'):
    data = {}
    not_ordered = []
    ordered = []
    sum_list = []
    drug_order = Drug_order()
    today = date.today()
    if request.method == "POST":
        emchilgee = Emchilgee.objects.filter(worker = request.user.worker)
        for item in emchilgee:
            drug_important = Drug_important.objects.filter(emchilgee = item)
            for drug in drug_important:
                drug.is_ordered = True
                drug.save()
                drug_order.name = drug.name
                drug_order.number = drug.shirheg
                drug_order.nurse = request.user.worker
                drug_order.save()

    emchilgee = Emchilgee.objects.filter(worker = request.user.worker)
    for item in emchilgee:
        drug_important = Drug_important.objects.filter(emchilgee = item)
        for drug in drug_important:
            if drug.is_ordered == False:
                not_ordered.append(drug)
            else:
                ordered.append(drug)
    ordered_order = Drug_order.objects.all()
    for items in ordered_order:
        pprint.pprint(items.id)
    data['ordered_order'] = ordered_order
    data['ordered'] = ordered
    data['not_ordered'] = not_ordered

    return render(request, template_name, data)

def add_recived_date(request, id):
    drug_order = get_object_or_404(Drug_order,id=id)
    drug_order.recived_date = date.today()
    drug_order.save()
    return redirect('drug:drug_order')

def reviews(request, template_name='drug/reviews.html'):
    data = {}
    temp = []
    today = date.today()
    emchilgee = Emchilgee.objects.filter(worker = request.user.worker)
    drug_important = Drug_important.objects.all()
    for item in emchilgee:
        if item.end_date < today:
            temp.append(item)

    emchilgee = temp
    data['drug_important'] = drug_important
    data['emchilgee'] = emchilgee

    return render(request, template_name, data)

def make_review_1(request, emchilgee_id):
    doctor_review = doctor_review.save(commit=False)

    doctor_review.emchilgee = emchilgee_id
    doctor_review.doctor = request.user.worker
    doctor_review.review = 1
    emchilgee.save()
    return redirect('drug:all_emchilgee_list')

def make_review_2(request, emchilgee_id):
    emchilgee = get_object_or_404(Emchilgee, id = emchilgee_id)
    emchilgee.doctor = request.user.worker
    emchilgee.doctor_review = 2
    emchilgee.save()
    return redirect('drug:all_emchilgee_list')

def make_review_3(request, emchilgee_id):
    emchilgee = get_object_or_404(Emchilgee, id = emchilgee_id)
    emchilgee.doctor = request.user.worker
    emchilgee.doctor_review = review
    emchilgee.save()
    return redirect('drug:all_emchilgee_list')

def make_review_4(request, emchilgee_id):
    emchilgee = get_object_or_404(Emchilgee, id = emchilgee_id)
    emchilgee.doctor = request.user.worker
    emchilgee.doctor_review = 4
    emchilgee.save()
    return redirect('drug:all_emchilgee_list')

def make_review_5(request, emchilgee_id):
    emchilgee = get_object_or_404(Emchilgee, id = emchilgee_id)
    emchilgee.doctor = request.user.worker
    emchilgee.doctor_review = 5
    emchilgee.save()
    return redirect('drug:all_emchilgee_list')
