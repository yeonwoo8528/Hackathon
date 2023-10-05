from django.conf.urls import include
from django.urls import path
from django.urls import re_path

from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('board', views.board, name="board"),
    path('game_reco', views.game_reco, name="game_reco"),
    path('reco', views.reco, name="reco"),
    path('board_insert',  views.board_insert, name="board_insert"),
    path('board_update', views.board_update, name="board_update")
]