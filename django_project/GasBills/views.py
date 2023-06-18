from django.shortcuts import render
from django.contrib import messages
from .models import ProvideGasMeterForm, NaturalGasReadingForm, CollectingGasBillsForm


def form_six(request):
    form = ProvideGasMeterForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return render(request, 'GasBills/form6.html')
    else:
        print(form.errors)


    return render(request, 'GasBills/form6.html')


def form_seven(request):
    form = NaturalGasReadingForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return render(request, 'GasBills/form7.html')
    else:
        print(form.errors)
    return render(request, 'GasBills/form7.html')


def form_eight(request):
    form = CollectingGasBillsForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return render(request, 'GasBills/form8.html')
    else:
        print(form.errors)

    return render(request, 'GasBills/form8.html')
