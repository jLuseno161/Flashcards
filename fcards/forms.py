from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class NewPostForm(forms.ModelForm):
    class Meta:
        model= Flashcard
        fields=['name','title','user','description','category','date']
        widgets={

        }