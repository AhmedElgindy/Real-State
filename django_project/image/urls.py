from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('download/<int:pk>/', views.download_image, name='download_image'),
]