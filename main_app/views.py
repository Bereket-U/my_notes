from pyexpat import model
from django.shortcuts import render
from django.views.generic.edit import CreateView
# from django.views.generic import ListView
from .models import Note

# Create your views here.

def home (request):
    notes = Note.objects.all()
    return  render(request, 'home.html', {'notes': notes})

class note_create(CreateView):
    model = Note
    fields = ['title', 'text']
    success_url = '/'

def note_detail (request, note_id):
    note = Note.objects.get(id = note_id)
    return  render(request, 'detail.html', {'note': note})