
from django.shortcuts import render, redirect
from .models import UploadedImage

def upload_image(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        uploaded_image = UploadedImage.objects.create(image=image)
    return render(request, 'room/image.html')

def download_image(request, pk):
    uploaded_image = UploadedImage.objects.get(pk=pk)
    return render(request, 'room/image_rooms.html', {'image': uploaded_image})
