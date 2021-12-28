from django.urls import path

from . import views
from .forms import LoginForm


urlpatterns = [
    path('', views.home_page, name='index'),
    path('terms/', views.terms_page, name='terms'),
]
