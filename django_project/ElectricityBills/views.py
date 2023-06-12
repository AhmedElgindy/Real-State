from django.shortcuts import render, HttpResponse

from .models import  PaymentForm, MeterRequestForm,PayBillsForm,LicenseRequestForm,ReconciliationRequestForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PaymentSerializer, MeterRequestSerializer, PayBillsSerializer, LicenseRequestSerializer, ReconciliationRequestSerializer
# Create your views here.


def provideElectricMeter(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'ElectricityBills/form1.html')
        else:
            form = PaymentForm()
        return render(request, 'ElectricityBills/form1.html', {'form': form,
                                                               })
    else:
        form = PaymentForm()
    return render(request, 'ElectricityBills/form1.html', {'form': form,
                                                           })



def form2(request):
    if request.method == 'POST':
        form = MeterRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'ElectricityBills/form2.html')
        else:
            print(form.errors)
            form = MeterRequestForm()
            render(request, 'ElectricityBills/form2.html', {'form': form})
    
    return render(request, 'ElectricityBills/form2.html', )


def form3(request):
    if request.method == 'POST':
        form = PayBillsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'ElectricityBills/form3.html')
        else:
            form = PayBillsForm()
        return render(request, 'ElectricityBills/form3.html', {'form': form,
                                                               })
    else:
        form = PayBillsForm()
        return render(request, 'ElectricityBills/form3.html')

def form4(request):
    if request.method == 'POST':
        form = LicenseRequestForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'ElectricityBills/form4.html')
        else:
            print(form.errors)
            return render(request,'ElectricityBills/form4.html')

    else:
        form = LicenseRequestForm()
        return render(request, 'ElectricityBills/form4.html')

def form5(request):
    if request.method == 'POST':
        form = ReconciliationRequestForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'ElectricityBills/form5.html')
        else:
            print(form.errors)
            return render(request,'ElectricityBills/form5.html')

    else:
        form = ReconciliationRequestForm()
        return render(request, 'ElectricityBills/form5.html')

# --------------------------------api views -----------------------------
@api_view(['POST'])
def create_payment(request):
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def create_meter_request(request):
    serializer = MeterRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def create_pay_bills(request):
    serializer = PayBillsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def create_license_request(request):
    serializer = LicenseRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def create_reconciliation_request(request):
    serializer = ReconciliationRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)