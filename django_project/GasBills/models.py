from django.db import models

# This Is For Form 6

ORIGIN_TYPES_CHOICES = [
    ('شقة سكنية','شقة سكنية'),
    ('فيلا','فيلا'),
    ('مجمع سكني','مجمع سكني'),
    ('مكتب','مكتب'),
    ('مستودع','مستودع'),
    ('اختر من القائمة التالية','اختر من القائمة التالية')
]
FACILITY_TYPES_CHOICES = [
    ('منزل','منزل'),
    ('شركة','شركة'),
    ('منشأة حكومية','منشأة حكومية'),
    ('برجاء تحديد المنشأ','برجاء تحديد المنشأ')
]

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
    origin_type = models.CharField(max_length=100, 
    choices=ORIGIN_TYPES_CHOICES,default='اختر من القائمة التالية')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self): 
        return self.name    
    

class NaturalGasReading(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)    
    national_identity_card_number = models.CharField(
        max_length=14, blank=False, null=False)
    last_reading= models.CharField(max_length=300, blank=False, null=False)
    last_reading_date = models.DateField()
    current_reading = models.CharField(max_length=300)
    counter_image = models.ImageField(upload_to='images/')
    origin_type = models.CharField(max_length=100, 
    choices=FACILITY_TYPES_CHOICES,default='برجاء تحديد المنشأ')
  

    def __str__(self): 
        return self.name    

            
    
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
