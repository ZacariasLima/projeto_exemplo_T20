from django.shortcuts import render
from utils.characters.factory import make_character

# Create your views here.
def home (request):
    return render (request, 'characters/pages/home.html', context={
        'characters': [make_character() for _ in range(10)],
    })

# Character detail
def character (request, id):
    return render (request, 'characters/pages/character-view.html', context={
        'character': make_character(),
        'is_it_detail': True 
    })