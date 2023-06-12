from django.db import models
from django import forms


class Payment(models.Model):
    codenumber = models.CharField(max_length=20)
    meterreding = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    comments = models.TextField()


    def __str__(self):
        return self.codenumber


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['codenumber', 'meterreding', 'company', 'comments', 'image']


class MeterRequest(models.Model):
    national_ID = models.IntegerField()
    name = models.CharField(max_length=50)
    meter_address = models.CharField(max_length=20)
    phone_num = models.IntegerField()
    address = models.CharField(max_length=30)
    block_num = models.IntegerField()
    phone_num2 = models.IntegerField()
    att_image = models.ImageField(upload_to='images/')
    id_image = models.ImageField(upload_to='images/')
    approvale_authority_name = models.CharField(max_length=50)
    approvale_authority = models.CharField(max_length=50)
    applicant = models.CharField(max_length=50)
    tax_num = models.IntegerField()
    Governorate = models.CharField(max_length=10)
    Enterprise = models.CharField(max_length=10)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class MeterRequestForm(forms.ModelForm):
    class Meta:
        model = MeterRequest
        fields = '__all__'


class PayBills(models.Model):
    number = models.IntegerField()
    company = models.CharField(max_length=20)
    comments = models.TextField()

    def __str__(self):
        return self.company

class PayBillsForm(forms.ModelForm):
    class Meta:
        model = PayBills
        fields = '__all__'

class LicenseRequest(models.Model):
    name = models.CharField(max_length=50)
    national_ID = models.IntegerField()
    national_ID2 =models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    governorate = models.CharField(max_length=10)
    region = models.CharField(max_length=30)
    phone_num= models.IntegerField()
    governorate =models.CharField(max_length=10)
    phone_num2 = models.IntegerField()
    block_number = models.IntegerField()
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    facility_type = models.CharField(max_length=30)
    authority = models.CharField(max_length=30)
    authority_name = models.CharField(max_length=30)
    latitude = models.DecimalField(max_digits=9, decimal_places=6,null= True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6 ,null=True)
    tax_number = models.IntegerField()
    applicant = models.CharField(max_length=30)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class LicenseRequestForm(forms.ModelForm):
    class Meta:
        model = LicenseRequest
        fields = "__all__"
class ReconciliationRequest(models.Model):
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

class ReconciliationRequestForm(forms.ModelForm):
    class Meta:
        model = ReconciliationRequest
        fields = "__all__"