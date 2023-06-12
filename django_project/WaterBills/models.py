from django.db import models


FACILITY_TYPES_CHOICES = [
    ('منزل', 'منزل'),
    ('شركة', 'شركة'),
    ('منشأة حكومية', 'منشأة حكومية'),
    ('برجاء تحديد المنشأ', 'برجاء تحديد المنشأ')
]


class WaterMeter(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)
    national_identity_card_number = models.CharField(
        max_length=14, blank=False, null=False)
    national_identity_card_photo = models.ImageField(upload_to='images/')
    copy_of_the_ownership_contract = models.ImageField(
        upload_to='images/')
    district_number = models.PositiveIntegerField()
    builging_license = models.ImageField(upload_to='images/')
    house_measurement = models.ImageField(upload_to='images/')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class WaterMeterReading(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)
    national_identity_card_number = models.CharField(
        max_length=14, blank=False, null=False)
    last_reading = models.CharField(max_length=300, blank=False, null=False)
    last_reading_date = models.DateField()
    current_reading = models.CharField(max_length=300)
    counter_image = models.ImageField(
        upload_to='images/')
    origin_type = models.CharField(max_length=100,
                                   choices=FACILITY_TYPES_CHOICES, default='برجاء تحديد المنشأ')

    def __str__(self):
        return self.name


class CollectingWaterBills(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)
    national_identity_card_number = models.CharField(
        max_length=14, blank=False, null=False)
    counter_image = models.ImageField(
        upload_to='images/')
    counter_number = models.CharField(max_length=20)
    neighborhood_number = models.PositiveIntegerField()
    governorate_number = models.PositiveIntegerField()
    another_counter_image = models.ImageField(
        upload_to='images/')

    def __str__(self):
        return self.name
