
from django.urls import path, include
from . import views
from.api_views import *
urlpatterns = [
    path("9", views.form_nine, name="form9"),
    path("10", views.form_ten, name="form10"),
    path("11", views.form_eleven, name="form11"),
    path("api/9/",WaterMeterView().as_view(),name="api_form9"),
    path("api/10/",WaterMeterReadingView().as_view(),name="api_form10"),
    path("api/11/",CollectingWaterBillsView().as_view(),name="api_form11"),

]
