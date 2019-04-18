from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError

from .models import Drug_category, Drug_detail, Drug_order, Drug_order_status, Drug_important, Emchilgee, Onosh, History
from .forms import Drug_detail_create_form, Drug_important_form, Emchilgee_form, OnoshForm, HistoryForm

# Create your views here.
def drug_detail_list(request, template_name='drug/drug_detail_list.html'):
    drug_detail = Drug_detail.objects.all()
    data = {}
    data['drug_detail'] = drug_detail
    return render(request, template_name, data)

def drug_detail_create(request, template_name='drug/drug_detail_create.html'):
    form = Drug_detail_create_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('drug:drug_detail_list')
    return render(request, template_name, {'form':form})

def emchilgee_create(request, template_name='drug/emchilgee_create.html'):
    context = {}
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

            return redirect('drug:emchilgee_list')

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

    emchilgee = Emchilgee.objects.all()
    drug_important = Drug_important.objects.all()

    data = {}
    data['drug_important'] = drug_important
    data['emchilgee'] = emchilgee

    return render(request, template_name, data)
