from django.db import models
from django import forms
# This Is For Form 6




class ProvideGasMeter(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)
    national_identity_card_number = models.CharField(
        max_length=14, blank=False, null=False)
    national_identity_card_photo = models.ImageField(upload_to='images/')
    copy_of_the_ownership_contract = models.ImageField(
        upload_to='images/')
    photo_of_recent_electricity_receipt = models.ImageField(
       upload_to='images/')
    receipt_of_approval_from_gas_company = models.ImageField(
       upload_to='images/')
    origin_type = models.CharField(max_length=100,)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self): 
        return self.name    

class ProvideGasMeterForm(forms.ModelForm):
    class Meta:
        model = ProvideGasMeter
        fields = "__all__"

class NaturalGasReading(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)    
    national_identity_card_number = models.CharField(
        max_length=14, blank=False, null=False)
    last_reading= models.CharField(max_length=300, blank=False, null=False)
    last_reading_date = models.DateField()
    current_reading = models.CharField(max_length=300)
    counter_image = models.ImageField(upload_to='images/')
    origin_type = models.CharField(max_length=100)
  

    def __str__(self): 
        return self.name    
    
class NaturalGasReadingForm(forms.ModelForm):
    class Meta:
        model = NaturalGasReading
        fields = "__all__"
            
    
class CollectingGasBills(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)    
    national_identity_card_number = models.CharField(
        max_length=14, blank=False, null=False)
    counter_image = models.ImageField(
       upload_to='images/')
    counter_number = models.CharField(max_length=20)
    neighborhood_number= models.PositiveIntegerField()
    governorate_number = models.PositiveIntegerField()
    another_counter_image = models.ImageField(
       upload_to='images/')
    
    def __str__(self): 
        return self.name  
class CollectingGasBillsForm(forms.ModelForm):
    class Meta:
        model = CollectingGasBills
        fields = "__all__"