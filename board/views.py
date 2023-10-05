from django.shortcuts import render
from board.models import Board
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from games.models import Games

# Create your views here.
def home(request):
    return render(request, "home.html")

def board(request):
    rsBoard = Board.objects.all()

    return render(request, "game.html", {
        'rsBoard': rsBoard
    })

def game_reco(request):
    return render(request, "game_reco.html")

def reco(request):
    game_data=Games.objects.all()
    sBoard = Board.objects.all()
    rsBoard = sBoard.last()
    context={"game_data":game_data, "rsBoard":rsBoard}
    return render(request, "reco.html",context)



def board_insert(request):
    bage=request.GET['b_age']
    bsex=request.GET['b_sex']
    bgenre=request.GET['b_genre']
    btime=request.GET['b_time']
    if bage!="":
        rows=Board.objects.create(b_age=bage,b_sex=bsex,b_genre=bgenre,b_time=btime)
        return redirect('/reco')
    else:
        return redirect('/game_reco')

def board_update(request):
    bno=request.GET['b_no']
    bage = request.GET['b_age']
    bsex = request.GET['b_sex']
    bgenre = request.GET['b_genre']
    btime = request.GET['b_time']

    try:
        board = Board.objects.get(b_no=bno)
        if bage != "":
            board.b_age = bage
        if bsex!="":
            board.b_sex=bsex
        if bgenre!="":
            board.b_genre=bgenre
        if btime!="":
            board.b_time=btime

        try:
            board.save()
            return redirect('/board')
        except ValueError:
            return HttpResponse({"success": False, "msg": "에러입니다."})

    except ObjectDoesNotExist:
        return HttpResponse({"success": False, "msg": "게시글 없음"})