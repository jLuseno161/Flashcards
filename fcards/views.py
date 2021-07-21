from django.db import models
from .models import *
from django.shortcuts import render

# Create your views here.
def index(request):
    flashcards= Flashcard.objects.all()
    return render(request, 'index.html',{"flashcards":flashcards})