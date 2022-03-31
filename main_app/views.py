from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Note

# Create your views here.

def home (request):
    return  render(request, 'home.html')


class NoteCteate(CreateView):
    model = Note
    fields = ['title', 'text']
    success_url = '/'
    