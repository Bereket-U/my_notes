from operator import imod
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/create', views.note_create.as_view(), name='notes_create'),
    
]