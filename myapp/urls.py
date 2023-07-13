from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('rules',views.rules,name="rules"),
    path('play',views.play,name="play"),
    path('profile',views.profile,name="profile"),
    path('get_result',views.get_result,name="get_result"),
    path('single_player',views.singleplayer,name="single_player"),
    path('multi_player',views.multiplayer,name="multi_player"),
    path('video_feed',views.video_feed,name='video_feed'),
]