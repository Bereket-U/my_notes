from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/create', views.NoteCteate.as_view(), name='notes_create')
]