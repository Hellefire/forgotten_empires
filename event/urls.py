from django.urls import path

from . import views


urlpatterns = [
    path('gameevents/', views.gameevent_list, name='gm_game_events'),
    path('shardevents/', views.shardevent_list, name='gm_shard_events'),
]
