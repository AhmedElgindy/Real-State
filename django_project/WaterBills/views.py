from django.shortcuts import render
from .models import WaterMeter, WaterMeterReading, CollectingWaterBills
from django.contrib import messages


def form_nine(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        national_identity_card_number = request.POST.get("national-id")
        national_identity_card_photo = request.POST.get("meter-image")
        copy_of_the_ownership_contract = request.POST.get(
            "meter-image-2")
        district_number = request.POST.get(
            "district-number")
        builging_license = request.POST.get(
            "meter-image-3")
        house_measurement = request.POST.get("last-reading-image")
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
            new_bill = WaterMeter(
                name=name,
                national_identity_card_number=national_identity_card_number,
                national_identity_card_photo=national_identity_card_photo,
                copy_of_the_ownership_contract=copy_of_the_ownership_contract,
                district_number=district_number,
                builging_license=builging_license,
                house_measurement=house_measurement,
                latitude=latitude,
                longitude=longitude,
            )
            new_bill.save()
            return render(request, 'WaterBills/form9.html')

    return render(request, 'WaterBills/form9.html')


def form_ten(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        national_identity_card_number = request.POST.get("id")
        last_reading = request.POST.get("last-reading")
        last_reading_date = request.POST.get("date")
        current_reading = request.POST.get("current-reading")
        counter_image = request.POST.get("image")
        origin_type = request.POST.get("type")

        # Perform validation
        if not name:
            messages.error(request, 'Please provide a name.')
        elif not national_identity_card_number:
            messages.error(
                request, 'Please provide a national identity card number.')
        # Add more validation conditions as needed

        # If there are no validation errors, save the data
        if not messages.get_messages(request):
            new_reading = WaterMeterReading(
                name=name,
                national_identity_card_number=national_identity_card_number,
                last_reading=last_reading,
                last_reading_date=last_reading_date,
                current_reading=current_reading,
                counter_image=counter_image,
                origin_type=origin_type
            )
            new_reading.save()
            return render(request, 'WaterBills/form10.html')

    return render(request, 'WaterBills/form10.html')


def form_eleven(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        national_identity_card_number = request.POST.get("national-id")
        counter_image = request.POST.get("meter-image")
        counter_number = request.POST.get("meter-number")
        neighborhood_number = request.POST.get("district-number")
        governorate_number = request.POST.get("governorate-number")
        another_counter_image = request.POST.get("last-reading-image")

        # Perform validation
        if not name:
            messages.error(request, 'Please provide a name.')
        elif not national_identity_card_number:
            messages.error(
                request, 'Please provide a national identity card number.')
        # Add more validation conditions as needed

        # If there are no validation errors, save the data
        if not messages.get_messages(request):
            add_reading = CollectingWaterBills(
                name=name,
                national_identity_card_number=national_identity_card_number,
                counter_image=counter_image,
                counter_number=counter_number,
                neighborhood_number=neighborhood_number,
                governorate_number=governorate_number,
                another_counter_image=another_counter_image
            )
            add_reading.save()
            return render(request, 'WaterBills/form11.html')

    return render(request, 'WaterBills/form11.html')
