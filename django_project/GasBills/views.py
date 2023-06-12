from django.shortcuts import render
from django.contrib import messages
from .models import ProvideGasMeter, NaturalGasReading, CollectingGasBills


def form_six(request):
    if request.method == 'POST':
        name = request.POST.get("full-name")
        national_identity_card_number = request.POST.get("national-id")
        national_identity_card_photo = request.POST.get("national-id-image")
        copy_of_the_ownership_contract = request.POST.get(
            "property-contract-image")
        photo_of_recent_electricity_receipt = request.POST.get(
            "electricity-receipt-image")
        receipt_of_approval_from_gas_company = request.POST.get(
            "property-image")
        origin_type = request.POST.get("facility-type")
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
            new_bill = ProvideGasMeter(
                name=name,
                national_identity_card_number=national_identity_card_number,
                national_identity_card_photo=national_identity_card_photo,
                copy_of_the_ownership_contract=copy_of_the_ownership_contract,
                photo_of_recent_electricity_receipt=photo_of_recent_electricity_receipt,
                receipt_of_approval_from_gas_company=receipt_of_approval_from_gas_company,
                origin_type=origin_type,
                latitude=latitude,
                longitude=longitude,
            )
            new_bill.save()
            return render(request, 'GasBills/form6.html')

    return render(request, 'GasBills/form6.html')


def form_seven(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        national_identity_card_number = request.POST.get("national-id")
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
            new_reading = NaturalGasReading(
                name=name,
                national_identity_card_number=national_identity_card_number,
                last_reading=last_reading,
                last_reading_date=last_reading_date,
                current_reading=current_reading,
                counter_image=counter_image,
                origin_type=origin_type
            )
            new_reading.save()
            return render(request, 'GasBills/form7.html')

    return render(request, 'GasBills/form7.html')


def form_eight(request):
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
            add_reading = CollectingGasBills(
                name=name,
                national_identity_card_number=national_identity_card_number,
                counter_image=counter_image,
                counter_number=counter_number,
                neighborhood_number=neighborhood_number,
                governorate_number=governorate_number,
                another_counter_image=another_counter_image
            )
            add_reading.save()
            return render(request, 'GasBills/form8.html')

    return render(request, 'GasBills/form8.html')
