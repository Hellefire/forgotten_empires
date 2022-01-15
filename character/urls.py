from django.urls import path

from . import views


urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list'),
    path('character_add/', views.character_add, name='character_add'),
    path('character_edit/', views.character_edit, name='character_edit'),
    path('character_update_gm/<int:character_id>/', views.character_update_gm, name='character_update_gm'),
    path('character_view/<int:pk>/', views.CharacterDetailView.as_view(), name='character_view'),
]
