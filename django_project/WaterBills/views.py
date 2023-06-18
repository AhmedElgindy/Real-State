from django.shortcuts import render
from .models import WaterMeter, WaterMeterReadingForm, CollectingWaterBillsForm
from django.contrib import messages



def form_nine(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        national_identity_card_number = request.POST.get("national-id")
        national_identity_card_photo = request.FILES.get("meter-image")
        copy_of_the_ownership_contract = request.FILES.get("meter-image-2")
        district_number = request.POST.get("district-number")
        builging_license = request.FILES.get("meter-image-3")
        house_measurement = request.FILES.get("last-reading-image")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")

        # Perform validation
        if not name:
            messages.error(request, 'Please provide a name.')
        elif not national_identity_card_number:
            messages.error(request, 'Please provide a national identity card number.')
        # Add more validation conditions as needed

        # If there are no validation errors, save the data
        if not messages.get_messages(request):
            new_bill = WaterMeter(
                name=name,
                national_identity_card_number=national_identity_card_number,
                national_identity_card_photo='images/' + national_identity_card_photo.name if national_identity_card_photo else None,
                copy_of_the_ownership_contract='images/' + copy_of_the_ownership_contract.name if copy_of_the_ownership_contract else None,
                district_number=district_number,
                builging_license='images/' + builging_license.name if builging_license else None,
                house_measurement='images/' + house_measurement.name if house_measurement else None,
                latitude=latitude,
                longitude=longitude,
            )
            new_bill.save()
            return render(request, 'WaterBills/form9.html')

    return render(request, 'WaterBills/form9.html')


def form_ten(request):
    form = WaterMeterReadingForm(request.POST , request.FILES )
    if form.is_valid():
            form.save()
            return render(request, 'WaterBills/form10.html')
    else:
            print(form.errors)

   
    
    return render(request, 'WaterBills/form10.html',)

def form_eleven(request):
    form = CollectingWaterBillsForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return render(request, 'WaterBills/form11.html')
    else:
         print(form.errors)
    
    return render(request, 'WaterBills/form11.html')

