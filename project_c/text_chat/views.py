from django.shortcuts import render
from .models import Room, Message

def index(request):
    rooms = Room.objects.all()
    return render(request, 'text_chat/index.html', {'rooms': rooms})

def room(request, room_name):
    room, created = Room.objects.get_or_create(name=room_name)
    messages = Message.objects.filter(room=room)[:100]
    
    return render(request, 'text_chat/room.html', {
        'room_name': room_name,
        'room': room,
        'messages': messages,
    })