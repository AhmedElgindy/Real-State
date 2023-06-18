from django.urls import path
from . import views

urlpatterns = [
    path('1/',views.provideElectricMeter,name='form1'),
    path('2/',views.form2,name='form2'),
    path('3/',views.form3,name='form3'),
    path('4/',views.form4,name='form4'),
    path('5/',views.form5,name='form5'),
    path('api/1',views.create_payment,name="api_form1"),
    path('api/2',views.create_meter_request,name="api_form2"),
    path('api/3',views.create_pay_bills,name="api_form3"),
    path('api/4',views.create_license_request,name="api_form4"),
    path('api/5',views.create_reconciliation_request,name="api_form5"),
]

