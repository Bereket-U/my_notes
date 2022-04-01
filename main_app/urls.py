from operator import imod
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/create', views.note_create.as_view(), name='notes_create'),
    path('notes/<int:note_id>',views.note_detail, name='note_detail' )
]