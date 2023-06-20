from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.views import (
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from users.views import *
from users.api_views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("api/password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    path(
        "api/password/reset/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path('api/user/',CustomUserDetailsView().as_view(),name='profile'),
    path('api/registration/',CustomRegisterView().as_view(),name='profile'),
    path("admin/", admin.site.urls),
    path("elec/", include('ElectricityBills.urls')),
    path("gas/", include('GasBills.urls')),
    path("buildings/", include('Buildings.urls')),
    path("water/", include('WaterBills.urls')),
    path('image/', include('image.urls')),
    path("services/", views.services, name='services'),
    path("index/", views.index, name='index'),
    path("contact/", views.contact, name='contact'),
    path("about/", views.about, name='about'),
    path("accounts/", include('allauth.urls')),
    path('chat/', include('room.urls')),
    path("newsignup/",newsignup), 
    path("newlogin/",newlogin,name='newlogin'),
    path("users/",include("users.urls")),
    path("api/",include('dj_rest_auth.urls')),
    path('api/registration/', include('dj_rest_auth.registration.urls')),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('dashboard/elec/',views.electricityServices,name="dashboard_elec"),
    path('dashboard/elec/dashelec1/',views.dashelec1,name="dashboard_elec1"),
    path('dashboard/elec/dashelec2/',views.dashelec2,name="dashboard_elec2"),
    path('dashboard/elec/dashelec3/',views.dashelec3,name="dashboard_elec3"),
    path('dashboard/water/',views.waterSerivces,name="dashboard_water"),    
    path('dashboard/water/dashwater1',views.dashwater1,name="dashboard_water1"),    
    path('dashboard/water/dashwater2',views.dashwater2,name="dashboard_water2"),    
    path('dashboard/water/dashwater3',views.dashwater3,name="dashboard_water3"),    
    path('dashboard/gas/',views.gasSerivces,name="dashboard_gas"),    
    path('dashboard/gas/dashgas1',views.dashgas1,name="dashboard_gas1"),    
    path('dashboard/gas/dashgas2',views.dashgas2,name="dashboard_gas2"),    
    path('dashboard/gas/dashgas3',views.dashgas3,name="dashboard_gas3"),    
    path('dashboard/building/',views.buildingSerivces,name="dashboard_building"),    
    path('dashboard/building/dashbuild1',views.dashbuild1,name="dashboard_building1"),    
    path('dashboard/building/dashbuild2',views.dashbuild2,name="dashboard_building2"),    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

