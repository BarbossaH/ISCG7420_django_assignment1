from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Room, Topic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RoomForm
from django.contrib import messages

# Create your views here. it seems router file
# this file is for our webpage function, but it must let urls in system knows this file's existence
from django.http import HttpResponse


def loginPage(request):
    pageName = "login"
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        # username = request.POST.get("username").lower()
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User not found")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or password is wrong")
    context = {"pageName": pageName}
    return render(request, "studyapp/login_register.html", context)


def logoutPage(request):
    logout(request)
    return redirect("home")


def registerPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # need to some change before save
            user = form.save(commit=False)
            # format the username
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Registration not succeeded ")
    return render(request, "studyapp/login_register.html", {"form": form})


# based on setting in system, after changing the DIRS, so it can load the files in templates folder
def home(request):
    # modelName.objects = model object attribute; modelName.objects = Method() such as get(), filter()
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    # print(q)
    rooms = Room.objects.filter(
        Q(topic__name__contains=q) | Q(name__icontains=q) | Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {"rooms": rooms, "topics": topics, "room_count": room_count}
    # send the Room object as a parameter to home.html
    return render(request, "studyapp/home.html", context)


def room(request, pk):
    # using the pk as the id to access to the corresponding room
    room = Room.objects.get(id=pk)
    context = {"room": room}
    return render(request, "studyapp/room.html", context)


@login_required(login_url="login")
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        # print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "studyapp/room_form.html", context)


@login_required(login_url="login")
def updateRoom(request, pk):
    # print(request.method)
    room = Room.objects.get(id=pk)
    # initialize the form with data from the room
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("You are not the host.")

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "studyapp/room_form.html", context)


@login_required(login_url="login")
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse("You are not the host.")
    if request.method == "POST":
        # delete from the database
        room.delete()
        return redirect("home")
    return render(request, "studyapp/delete.html", {"obj": room})
