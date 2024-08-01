from django.shortcuts import render, HttpResponse, redirect
from game.models import *
from django.contrib import messages

from django.shortcuts import render
from django.http import JsonResponse
import sys

emptyCell = ''
maxScore = 10
minScore = -10
isPersonTurn = False
computerSymbol = ''
personSymbol = ''
invalidPosition = -1

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    elif request.method == "POST":
        roomId = request.POST.get("room-id", None)
        playerName = request.POST.get("player-name", "Unknown")
        if(roomId):
            try:
                room = Room.objects.get(id=roomId)
                return redirect(f"/game/{room.id}/{playerName}/")
            except Room.DoesNotExist:
                messages.error(request, "Room does not exist")
                return redirect("/")
        else:
            room = Room.objects.create()
            return redirect(f"/game/{room.id}/{playerName}/")


def game(request, id=None, name=None):
    try:
        room = Room.objects.get(id=id)
        return render(request, "game.html", {"room": room, "name": name})
    except Room.DoesNotExist:
        messages.error(request, "Room does not exist")
        return redirect("/")
    
