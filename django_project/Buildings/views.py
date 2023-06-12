from django.shortcuts import render
from django.contrib import messages
from .models import BuildingPermitApplications, CollectingReconciliationBuilding
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BuildingPermitApplicationsSerializer, CollectingReconciliationBuildingSerializer
from django.views.decorators.http import require_GET
from django.http import JsonResponse

def form_twelve(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        national_identity_card_number = request.POST.get("national-id")
        national_identity_card_photo = request.POST.get("meter-image")
        agricultural_basin_number = request.POST.get("meter-number")
        documents_ownership = request.POST.get("meter-image-2")
        phone_number = request.POST.get("governorate-number")
        agricultural_approval = request.POST.get("last-reading-image")
        approval_photos = request.POST.get("last-reading-image-3")
        space = request.POST.get("governorate-number-2")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        

        # Perform validation
        if not name:
            messages.error(request, 'Please provide a name.')
        elif not national_identity_card_number:
            messages.error(
                request, 'Please provide a national identity card number.')
        # Add more validation conditions as needed

        # If there are no validation errors, save the data
        if not messages.get_messages(request):
            new_app = BuildingPermitApplications(
                name=name,
                national_identity_card_number=national_identity_card_number,
                national_identity_card_photo=national_identity_card_photo,
                agricultural_basin_number=agricultural_basin_number,
                documents_ownership=documents_ownership,
                phone_number=phone_number,
                agricultural_approval=agricultural_approval,
                approval_photos=approval_photos,
                space=space,
                latitude=latitude,
                longitude=longitude,
            )
            new_app.save()
            return render(request, 'Buildings/form12.html')

    return render(request, 'Buildings/form12.html')


def form_thirteen(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        national_identity_card_number = request.POST.get("national-id")
        national_identity_card_photo = request.POST.get("meter-image")
        agricultural_basin_number = request.POST.get("meter-number")
        violation_request = request.POST.get("meter-image-2")
        phone_number = request.POST.get("governorate-number")
        violation_request_eng = request.POST.get("last-reading-image")
        approval_photos = request.POST.get("last-reading-image-2")
        space = request.POST.get("governorate-number-2")
       
        # Perform validation
        if not name:
            messages.error(request, 'Please provide a name.')
        elif not national_identity_card_number:
            messages.error(
                request, 'Please provide a national identity card number.')
        # Add more validation conditions as needed

        # If there are no validation errors, save the data
        if not messages.get_messages(request):
            new_app = CollectingReconciliationBuilding(
                name=name,
                national_identity_card_number=national_identity_card_number,
                national_identity_card_photo=national_identity_card_photo,
                agricultural_basin_number=agricultural_basin_number,
                violation_request=violation_request,
                phone_number=phone_number,
                violation_request_eng=violation_request_eng,
                approval_photos=approval_photos,
                space=space,
           
            )
            new_app.save()
            return render(request, 'Buildings/form13.html')

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

