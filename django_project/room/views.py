from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
from .models import Room, Message


@login_required
def room(request, slug):
    print(slug)
    room = get_object_or_404(Room, slug=slug)
    messages = Message.objects.filter(room=room)[:25]
    return render(request, 'room/room.html', {'room': room, 'messages': messages})

@login_required
def profile(request):
    return render(request, 'room/user.html', {'user': request.user})

@login_required
@user_passes_test(lambda user: user.is_superuser)
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})


