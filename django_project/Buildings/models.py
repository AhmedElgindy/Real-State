from django.db import models


class BuildingPermitApplications(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)
    national_identity_card_number = models.CharField(
        max_length=14, blank=False, null=False)
    national_identity_card_photo = models.ImageField(upload_to='images/')
    agricultural_basin_number = models.IntegerField()
    documents_ownership = models.ImageField(upload_to='images/')
    phone_number = models.IntegerField(null=True, blank=True)
    agricultural_approval = models.ImageField(upload_to='images/')
    approval_photos = models.ImageField(upload_to='images/')
    space = models.CharField(max_length=500)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    approved = models.BooleanField(null=True)
    def __str__(self):
        return self.name


class CollectingReconciliationBuilding(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)
    national_identity_card_number = models.CharField(
        max_length=14, blank=False, null=False)
    national_identity_card_photo = models.ImageField(upload_to='images/')
    agricultural_basin_number = models.IntegerField()
    violation_request = models.ImageField(upload_to='images/')
    phone_number = models.IntegerField(null=True, blank=True)
    violation_request_eng = models.ImageField(upload_to='images/')
    approval_photos = models.ImageField(upload_to='images/')
    space = models.CharField(max_length=500)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    approved = models.BooleanField(null=True)


    def __str__(self) -> str:
        return self.name
