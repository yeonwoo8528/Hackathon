from django.conf.urls import include
from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    path('games', views.games, name="games"),
]