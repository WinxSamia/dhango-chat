from django.shortcuts import render,redirect
from chat.models import Room,Messages
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def room(request, room):
    username=request.GET.get('username')
    room_derails=Room.objects.get(name=room)
    return render(request,'room.html',
    {
        'username': username,
        'room': room,
        'room_details': room_derails
    })
def checkview(request):
    room= request.POST['room_name']
    username=request.POST['username']
    if Room.objects.filter(name=room).exists():
       return redirect('/'+room+'/?username=/'+username)
    else:
        new_room=Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username=/'+username)
def sent(request):
    messages=request.POST['message']
    username=request.POST['username']
    room_id=request.POST['room_id']
    new_message=messages.objects.create(value=messages, user=username,room_id=room_id)
    messages.save()
    return HttpResponse('Message sent successfully')
def getMessages(request, room):
    room_details=Room.objects.get(name=room)
    messages=Messages.objects.filter(room=room_details.id)
    return JsonResponse({'messages':list(messages.values())})
