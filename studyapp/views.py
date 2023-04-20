from django.shortcuts import render

from .models import Room

# Create your views here.
# this file is for our webpage function, but it must let urls in system knows this file's existence
from django.http import HttpResponse


# based on setting in system, after changing the DIRS, so it can load the files in templates folder
def home(request):
    # modelName.objects = model object attribute; modelName.objects = Method() such as get(), filter()
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    # send the Room object as a parameter to home.html
    return render(request, "studyapp/home.html", context)


def room(request, pk):
    # using the pk as the id to access to the corresponding room
    room = Room.objects.get(id=pk)
    context = {"room": room}
    return render(request, "studyapp/room.html", context)
