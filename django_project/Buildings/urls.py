from django.urls import path, include
from . import views
urlpatterns = [
    path("12", views.form_twelve, name="form12"),
    path("13", views.form_thirteen, name="form13"),
    path("api/12",views.create_building_permit_application,name="api12"),
    path("api/13",views.create_collecting_reconciliation_building,name="api14"),
    path('first-model/approved/', views.first_model_approved, name='first_model_approved'),
    path('first-model/not-approved/', views.first_model_not_approved, name='first_model_not_approved'),
    path('second-model/approved/', views.second_model_approved, name='second_model_approved'),
    path('second-model/not-approved/', views.second_model_not_approved, name='second_model_not_approved'),
    
]
