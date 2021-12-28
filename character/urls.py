from django.urls import path

from . import views


urlpatterns = [
    path('gm_characters/', views.gm_character_list, name='gm_characters'),
]
