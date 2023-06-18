from django.shortcuts import render
from django.contrib import messages
from .models import BuildingPermitApplicationsForm, CollectingReconciliationBuildingForm,BuildingPermitApplications,CollectingReconciliationBuilding
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BuildingPermitApplicationsSerializer, CollectingReconciliationBuildingSerializer
from django.views.decorators.http import require_GET
from django.http import JsonResponse

def form_twelve(request):
    form = BuildingPermitApplicationsForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return render(request, 'Buildings/form12.html')
    else:
        print(form.errors)
    return render(request, 'Buildings/form12.html')


def form_thirteen(request):
    form = CollectingReconciliationBuildingForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return render(request, 'Buildings/form13.html')
    else:
        print(form.errors)
    return render(request, 'Buildings/form13.html')

@api_view(['POST'])
def create_building_permit_application(request):
    serializer = BuildingPermitApplicationsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_collecting_reconciliation_building(request):
    serializer = CollectingReconciliationBuildingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@require_GET
def first_model_approved(request):
    applications = BuildingPermitApplications.objects.filter(approved=True)
    data = [{'latitude': app.latitude, 'longitude': app.longitude} for app in applications]
    return JsonResponse(data, safe=False)

@require_GET
def first_model_not_approved(request):
    applications = BuildingPermitApplications.objects.filter(approved=False)
    data = [{'latitude': app.latitude, 'longitude': app.longitude} for app in applications]
    return JsonResponse(data, safe=False)

@require_GET
def second_model_approved(request):
    buildings = CollectingReconciliationBuilding.objects.filter(approved=True)
    data = [{'latitude': building.latitude, 'longitude': building.longitude} for building in buildings]
    return JsonResponse(data, safe=False)

@require_GET
def second_model_not_approved(request):
    buildings = CollectingReconciliationBuilding.objects.filter(approved=False)
    data = [{'latitude': building.latitude, 'longitude': building.longitude} for building in buildings]
    return JsonResponse(data, safe=False)


	