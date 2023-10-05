from django.shortcuts import render
from games.models import Games

# Create your views here.
def games(request):
    rsGames = Games.objects.all()

    return render(request, "game.html", {
        'rsGames': rsGames
    })